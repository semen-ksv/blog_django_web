from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_posts_list, name='blog_home'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tags_list, name='tags_list'),
    path('tag/<str:slug>', tag_detail, name='tag_detail')
]


# TODO: отображение Тегов в постах не работает

