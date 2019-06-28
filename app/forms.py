from django import forms
from .models import Post, Topic, Community


class PostForm(forms.ModelForm):
    # this def for remove label
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = ''

    class Meta:
        model = Post
        fields = ['message', ]



class TopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 10, 'placeholder': 'ماذا يجول بخاطرك؟.'}
    ), max_length=4000)

    class Meta:
        model = Topic
        fields = ['community', 'subject', 'message']



class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ['name', 'description']
