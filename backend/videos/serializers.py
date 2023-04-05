from rest_framework import serializers
from .models import Video, Comment, Like


class VideoSerializer(serializers.ModelSerializer):
    video = serializers.FileField()
    class Meta:
        model = Video
        fields = ('user', 'title', 'video', 'slug', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'slug', 'created_at', 'updated_at')



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('user', 'video', 'created_at',)
        read_only_fields = ('user', 'video', 'created_at',)



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'video', 'comment', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'video',)