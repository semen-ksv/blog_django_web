from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsList.as_view(), name='blog_home'),
    path('search/', search, name='search_home'),
    path('user/<str:username>/', AuthorPostsList.as_view(), name='author_post'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('post/comment/<int:pk>/', AddComment.as_view(), name='post_comment'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('tags/', TagsList.as_view(), name='tags_list'),
    path('tags/create/', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete'),
    path('photo/', AllPhotography.as_view(), name='photography')
]
