from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name="search"),

    path('vote_post/<int:post_id>', views.vote_post, name="vote_post"),
    path('vote_comment/<int:comment_id>', views.vote_comment, name="vote_comment"),
    
    path('posts/<int:community_id>/', views.posts, name="posts"),
    
    path('post/<int:id>/', views.post, name="post"),
    path('post/add/', views.add_post),
    path('post/add/<int:community_id>/', views.add_post, name="add_post"),
    path('post/<int:id>/edit/', views.update_post, name="update_post"),
    
    path('communities/', views.communities, name="communities"),
    path('community/add/', views.add_community, name="add_community"),
    ]