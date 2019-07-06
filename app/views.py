from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


from .models import User, Community, Post , Comment
from .forms import PostForm, CommunityForm , CommentForm 



def posts(request, community_id=None):
    communities = Community.objects.all()
    if community_id:
        community = get_object_or_404(Community, pk=community_id)
        all_posts = community.posts.all()
    else:
        community = None
        all_posts = Post.objects.all()

    paginator = Paginator(all_posts, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {'posts':posts, 'communities':communities, 'this_community':community}
    return render(request, 'app/posts.html', context)


def post(request, id):
    post = get_object_or_404(Post, pk=id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.created_by = request.user
        comment.post = post
        comment.save()

        return redirect('post', post.id)
    context = {'post':post, 'form':form}
    return render(request, 'app/post.html', context)


def communities(request):
    communities = Community.objects.all()
    context = {'communities':communities}
    return render(request, 'app/communities.html', context)


def search(request, query):
    pass


@login_required
def add_post(request):
    form = PostForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        post = form.save(commit=False)
        post.created_by = request.user
        post.save()

        messages.success(request, 'نُشِر موضوعك')
        return redirect('post', post.id)
    return render(request, 'app/add_post.html', context)


def update_post(request, id):
    post = get_object_or_404(Post, pk=id)
    form = PostForm(request.POST)
    if form.is_valid():
        post.title = form.cleaned_data['title']
        post.content = form.cleaned_data['content']
        post.save()
        messages.success(request, 'عُدل موضوعك')
        return redirect('post', post.id)
    
    form = PostForm(instance=post)
    context = {'form':form, 'post':post}
    return render(request, 'app/add_post.html', context)



# @login_required
def add_community(request):
    if request.method == 'POST':
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save()
            messages.success(request, 'أٌنشِأ المجتمع الجديد')
            return redirect('posts', community.id)
    form = CommunityForm()
    context = {'form': form}

    return render(request, 'app/new_community.html', context)

# home page is posts url
home = posts