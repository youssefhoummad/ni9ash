from django import forms
from django.contrib.auth.models import User

from .models import Community, Post, Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''

    class Meta:
        model = Comment
        fields = ['content']



class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['community'].label = 'مجتمع'
        self.fields['title'].label = 'العنوان'
        self.fields['content'].label = ''

    class Meta:
        model = Post
        fields = ['community', 'title', 'content']



class CommunityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommunityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'اسم المجتمع'
        self.fields['description'].label = 'وصف'
    
    class Meta:
        model = Community
        fields = ['name', 'description']
