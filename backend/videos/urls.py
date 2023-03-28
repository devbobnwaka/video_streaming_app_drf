from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoAPIView.as_view(), name='video')
]