from django.urls import path
from .views import *


urlpatterns = [
    path('', blog_posts_list, name='blog_home'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
 ]

