import textwrap

from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

from markdown import markdown



# Create your models here.
class Community(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Topic(models.Model):
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    community = models.ForeignKey(Community, related_name='topics', on_delete=models.CASCADE)


    def __str__(self):
        return self.subject
    
    def get_message(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))




class Comment(models.Model):
    message = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, related_name='comments', on_delete=models.CASCADE)

    def has_child(self):
        if self.comments.exists():
            return True
        return False
    
    def has_parent(self):
        if self.parent.exists():
            return True
        return False


    def __str__(self):
        return textwrap.shorten(self.message, width=450, placeholder="...")


    def get_message(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
