from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Like
from .serializers import LikeSerializer
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        if Like.objects.filter(user=user, post=post).exists():
            return Response({"detail": "You already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=user, post=post)

        # Create a notification
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked."}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        like = Like.objects.filter(user=user, post=post)

        if not like.exists():
            return Response({"detail": "You haven't liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({"detail": "Post unliked."}, status=status.HTTP_200_OK)
