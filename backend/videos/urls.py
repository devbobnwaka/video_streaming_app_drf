from django.urls import path
from . import views

urlpatterns = [
    path('video/', views.VideoAPIView.as_view(), name='video-list'),
    path('video/<slug:slug>/', views.VideoAPIView.as_view(), name='video-detail'),
    path('video-auth/<slug:slug>/', views.VideoAuthenticatedAPIView.as_view(), name='video-auth'),
    # comments
    path('comment/', views.CommentAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', views.CommentAPIView.as_view(), name='comment-detail'),
    #video comments
    path('comment-auth/<slug:video_slug>/', views.CommentAuthenticatedAPIView.as_view(), name='comment-auth'),
    #video likes
    path('like-auth/<slug:video_slug>/', views.LikeAPIView.as_view(), name='like-list'),
    path('like-auth/<slug:video_slug>/', views.LikeAuthenticatedAPIView.as_view(), name='like-auth-post'),
]