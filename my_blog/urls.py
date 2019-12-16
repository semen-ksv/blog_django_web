from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_posts_list, name='blog_home'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('tags/', tags_list, name='tags_list'),
    path('tags/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update')
]
