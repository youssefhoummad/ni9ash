from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation

from markdown import markdown



class Vote(models.Model):
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
        )
    
    created_by = models.ForeignKey(User, related_name='votes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')





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
    votes = GenericRelation(Vote)

    def votes_count(self):
        ups = self.votes.filter(activity_type=Vote.UP_VOTE).count()
        downs = self.votes.filter(activity_type=Vote.DOWN_VOTE).count()
        return ups - downs
    
    def vote_up(self, user): 
        self.votes.create(activity_type=Vote.UP_VOTE, created_by=user)
    
    def vote_down(self, user): 
        self.votes.create(activity_type=Vote.DOWN_VOTE, created_by=user)

    def content_type(self):
        return ContentType.objects.get_for_model(self)

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
    votes = GenericRelation(Vote)

    def votes_count(self):
        ups = self.votes.filter(activity_type=Vote.UP_VOTE).count()
        downs = self.votes.filter(activity_type=Vote.DOWN_VOTE).count()
        return ups - downs
    
    def vote_up(self, user): 
        self.votes.create(activity_type=Vote.UP_VOTE, created_by=user)
    
    def vote_down(self, user):
        self.votes.create(activity_type=Vote.DOWN_VOTE, created_by=user)

    def content_type(self):
        return ContentType.objects.get_for_model(self)

    def __str__(self):
        return self.content
    
    def markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    
    class Meta:
        ordering = ['-created_at']
    
