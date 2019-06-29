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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    community = models.ForeignKey(Community, related_name='topics', on_delete=models.CASCADE)


    def __str__(self):
        return self.subject




class Post(models.Model):
    message = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    votes_pos = models.IntegerField(default=0)
    votes_neg = models.IntegerField(default=0)


    def votes(self):
        return self.votes_pos - self.votes_neg


    def __str__(self):
        return textwrap.shorten(self.message, width=450, placeholder="...")


    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
