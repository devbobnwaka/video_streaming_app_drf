from rest_framework import serializers
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('user', 'title', 'video', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'created_at', 'updated_at')