from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

from markdown import markdown


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

    def comments(self):
        return self.all_comments.filter(parent=None)

    def __str__(self):
        return self.title

    def markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='all_comments', on_delete=models.CASCADE)
    content = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.content
    
    def markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    
    class Meta:
        ordering = ['-created_at']
    
