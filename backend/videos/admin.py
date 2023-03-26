from django.contrib import admin
from .models import Video, Comment, Like

# Register your models here.

class LikeInline(admin.StackedInline):
    model = Like
    raw_id_fields = ('user', 'video')
    extra = 0

class CommentInline(admin.StackedInline):
    model = Comment
    raw_id_fields = ('user',)
    extra = 1

# @admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    inlines = (CommentInline, LikeInline, )
    raw_id_fields = ('user',)
    readonly_fields = ('created_at', 'updated_at')



admin.site.register(Video, VideoAdmin)
admin.site.register(Comment)
admin.site.register(Like)