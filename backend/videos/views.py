from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, response, authentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import VideoSerializer, CommentSerializer, LikeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Video, Comment, Like
from .mixins import MultipleFieldLookupMixin

# Create your views here.
class VideoAPIView( mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, 
                    generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
    # authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        if slug:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     user = request.user
    #     if not user.is_authenticated:
    #         return Video.objects.none()
        # if user.is_admin:
        #     return Video.objects.all()
        # print(request.user) 
        # return qs.filter(user=request.user)


class VideoAuthenticatedAPIView( mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentAPIView( mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)


class CommentAuthenticatedAPIView( mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        video_slug = self.kwargs.get('video_slug')
        instance = Video.objects.get(slug=video_slug)
        serializer.save(user=user, video=instance)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



class LikeAPIView( mixins.ListModelMixin, 
                    generics.GenericAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        # modify the queryset as needed
        video_slug = self.kwargs.get('video_slug')
        if video_slug:
            video_instance = Video.objects.get(slug=video_slug)
        return queryset.filter(video=video_instance)


class LikeAuthenticatedAPIView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None, *args, **kwargs, ):
        video_slug = self.kwargs.get('video_slug')
        if video_slug:
            serializer = LikeSerializer(data=request.data)
            if serializer.is_valid():
                video_instance = Video.objects.get(slug=video_slug)
                like_qs = Like.objects.filter(video=video_instance, user=request.user)
                if like_qs.exists():
                    like_qs.first().delete()
                    return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
                else:
                    serializer.save(user=request.user, video=video_instance)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "video_slug does not exist"}, status=status.HTTP_400_BAD_REQUEST)