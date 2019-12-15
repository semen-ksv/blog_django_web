from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_posts_list, name='blog_home'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tags/create', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>', TagDetail.as_view(), name='tag_detail')
]



