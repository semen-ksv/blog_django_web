from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_posts_list, name='blog_home'),
 ]

