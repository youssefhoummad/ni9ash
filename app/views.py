from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User, Community, Topic, Post
from .forms import PostForm, TopicForm, CommunityForm



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
    posts = topic.posts.all() 
    context = {'topic':topic, 'posts':posts}

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_by = request.user
            post.topic = topic
            post.save()

            return redirect('topic', topic.id)
    else:
        form = PostForm()
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
            topic.created_by = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user
            )
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
            form.save()
 
            return redirect('home') # TODO redirect to community page
    else:
        form = CommunityForm()
        context = {'form': form}

    return render(request, 'app/new_community.html', context)
