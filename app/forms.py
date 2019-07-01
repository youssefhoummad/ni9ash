from django import forms
from .models import Comment, Topic, Community


class CommentForm(forms.ModelForm):

    # this def for remove label
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['message'].label = ''
     
    #Hidden value to get a child's parent
    parent = forms.CharField(widget=forms.HiddenInput(
                            attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comment
        fields = ['message', 'parent']



class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['community', 'subject', 'message']



class CommunityForm(forms.ModelForm):

    class Meta:
        model = Community
        fields = ['name', 'description']
