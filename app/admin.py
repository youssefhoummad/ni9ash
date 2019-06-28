from django.contrib import admin

from .models import Community, Topic, Post

# Register your models here.
admin.site.register(Community)
admin.site.register(Topic)
admin.site.register(Post)
