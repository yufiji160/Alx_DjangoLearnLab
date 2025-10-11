from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
     post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
     content = models.TextField()
     created_at = models.DateTimeField(default=timezone.now)
     updated_at = models.DateTimeField(auto_now=True)


     class Meta:
         ordering = ['created_at']


     def __str__(self):
         return f"Comment by {self.author} on {self.post}"