from django.db import models
from django.contrib.auth.models import User



class Community(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Post(models.Model):
    community = models.ForeignKey(Community, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-created_at']
    
