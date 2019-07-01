from django.contrib import admin

from .models import Community, Topic, Comment

# Register your models here.
admin.site.register(Community)
admin.site.register(Topic)
admin.site.register(Comment)
