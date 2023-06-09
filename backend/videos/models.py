import uuid
from django.utils.text import slugify
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings

User=settings.AUTH_USER_MODEL

# Create your models here.
class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = CloudinaryField(resource_type='video')
    slug = models.SlugField(max_length=255, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) ->str:
        return self.user.first_name


    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(f'{self.title}{uuid.uuid4()}')
        super().save(*args, **kwargs)
        if self.slug is None:
            self.slug = slugify(f'{self.title}{uuid.uuid4()}')
            self.save()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.first_name

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.user.first_name


    
