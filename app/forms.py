from django import forms
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from .models import Community, Post, Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ''
        self.fields['content_type'].widget = forms.HiddenInput()
        self.fields['object_id'].widget = forms.HiddenInput()

    class Meta:
        model = Comment
        fields = ['content', 'content_type', 'object_id']

    
    def save(self, user, commit=True):
        instance = super(CommentForm, self).save(commit=False)
        instance.created_by = user
        # instance.content_type = ContentType.objects.get_for_model(
        #     model=self.cleaned_data.get('content_type'))
        instance.save()
        return instance



class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['community'].label = 'مجتمع'
        self.fields['title'].label = 'العنوان'
        self.fields['content'].label = ''

    class Meta:
        model = Post
        fields = ['community', 'title', 'content']

    def save(self, user, commit=True):
        instance = super(PostForm, self).save(commit=False)
        instance.created_by = user
        instance.save()
        return instance



class CommunityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommunityForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'اسم المجتمع'
        self.fields['description'].label = 'وصف'
    
    class Meta:
        model = Community
        fields = ['name', 'description']
