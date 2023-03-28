from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, mixins
from .serializers import VideoSerializer
from .models import Video

# Create your views here.
class VideoAPIView( mixins.ListModelMixin, 
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin, 
                    generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        if slug:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class VideoAuthenticatedAPIView( mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)