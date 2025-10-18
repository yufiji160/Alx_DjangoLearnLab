from django.urls import path
from .views import FeedView
from django.urls import path
from .views import LikePostView, UnlikePostView

urlpatterns = [
    path('feed/', FeedView.as_view(), name='feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]
