from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Community, Topic, Comment
from .forms import CommentForm, TopicForm, CommunityForm



def home(request):
    topics = Topic.objects.all()
    context = {'topics':topics, }
    return render(request, 'app/home.html', context)


def community(request, community_id):
    community = get_object_or_404(Community, pk=community_id)
    topics = community.topics.all()
    context = {'community':community, 'topics':topics}
    return render(request, 'app/community.html', context)


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    comments = topic.comments.all() 
    context = {'topic':topic, 'comments':comments}

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_by = request.user
            comment.topic = topic
            comment.save()            
            messages.success(request, 'نُشِر تعليقك')
            return redirect('topic', topic.id)
    else:
        form = CommentForm()
        context['form'] = form
    return render(request, 'app/topic.html', context)


def search(request, query):
    pass


@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.message = form.cleaned_data.get('message')
            topic.created_by = request.user
            topic.save()

            messages.success(request, 'نُشِر موضوعك')
            return redirect('topic', topic.id)
    else:
        form = TopicForm()
        context = {'form': form}

    return render(request, 'app/new_topic.html', context)


@login_required
def new_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            messages.success(request, 'أٌنشِأ المجتمع الجديد')
            return redirect('community', community.id) # temp some probleme if two user create  
    else:                                                                    # community in some time
        form = CommunityForm()
        context = {'form': form}

    return render(request, 'app/new_community.html', context)
