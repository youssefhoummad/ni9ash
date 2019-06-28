from django.urls import path


from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name="search"),
    path('topic/<int:topic_id>/', views.topic, name="topic"),
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_community/', views.new_community, name="new_community"),
    # path('cart/', views.cart, name="cart"),
    ]