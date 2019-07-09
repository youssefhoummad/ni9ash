from django.contrib import admin

from .models import Community, Post, Comment, Vote

# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by']
    list_filter = ['created_by', 'community']
    search_fields = ['title']
    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
admin.site.register(Community)
admin.site.register(Comment)
admin.site.register(Vote)
