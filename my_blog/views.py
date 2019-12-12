from django.shortcuts import render
from .models import Post, Tag


def blog_posts_list(request):
    """Create main page in blog page"""
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'my_blog/blog_post_list.html', context={'posts': posts})

def post_detail(request, slug):
    """Create page with post content"""
    if request.method == 'GET':
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'my_blog/post_detail.html', context={'post': post})

def tags_list(request):

    tags = Tag.objects.all()
    print(tags)
    return render(request, 'my_blog/tag_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'my_blog/tag_detail.html', context={'tag': tag})
