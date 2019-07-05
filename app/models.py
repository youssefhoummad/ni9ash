from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




# Create your models here.
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
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def comments(self):
        return Comment.objects.filter(content_type=self.content_type, object_id=self.id)
    
    @property
    def content_type(self):
        return ContentType.objects.get_for_model(self.__class__)

    


class Comment(models.Model):
    content = models.TextField(max_length=4000)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    # generic relations (google it)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # null must be del
    object_id = models.PositiveIntegerField() # null must be del
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.content
