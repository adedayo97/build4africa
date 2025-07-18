# news/urls.py
from django.urls import path
from . import views

app_name = 'news'  # This defines the namespace

urlpatterns = [
    path('', views.index, name='index'),
    path('press-releases/', views.press_releases, name='press_releases'),
    path('news/', views.news_media, name='news_media'),
    path('blog/', views.blog, name='blog'),
    path('blog/', views.blog, name='blog_list'),  # This is the missing URL pattern
    path('events/', views.events, name='events'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/<slug:slug>/', views.post_detail, name='post_detail'),  # For individual posts

]