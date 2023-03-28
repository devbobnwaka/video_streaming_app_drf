from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoAPIView.as_view(), name='video'),
    path('video-auth/', views.VideoAuthenticatedAPIView.as_view(), name='video-auth'),
    path('video/<slug:slug>/', views.VideoAPIView.as_view(), name='video-retrieve'),
    path('video-auth/<slug:slug>/', views.VideoAuthenticatedAPIView.as_view(), name='video-auth-retrieve'),
]