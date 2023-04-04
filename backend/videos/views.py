from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins, response, authentication
# from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import VideoSerializer, CommentSerializer
from .models import Video, Comment

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

