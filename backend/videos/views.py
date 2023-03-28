from rest_framework import generics, mixins
from .serializers import VideoSerializer
from .models import Video

# Create your views here.
class VideoAPIView( mixins.ListModelMixin, 
                    generics.GenericAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def get(self, request, *args, **kwargs):
        print(*args, **kwargs)
        return self.list(request, *args, **kwargs)