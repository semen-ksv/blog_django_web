from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post contentFirst post contentFirst post contentFirst post contentFirst post contentFirst post contentFirst post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content Second post content Second post content Second post content Second post content Second post content Second post content Second post content ',
#         'date_posted': 'August 28, 2018'
#     },
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post contentFirst post contentFirst post contentFirst post contentFirst post contentFirst post contentFirst post content',
#         'date_posted': 'August 27, 2018'
#     },
#     {
#         'author': 'Jane Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content Second post content Second post content Second post content Second post content Second post content Second post content Second post content ',
#         'date_posted': 'August 28, 2018'
#     },
#  ]

def blog_posts_list(request):
    """Create main page in blog page"""
    if request.method == 'GET':
        # context = {
        #     'posts': posts
        # }

        posts = Post.objects.all()

        return render(request, 'my_blog/blog_post_list.html', context={'posts': posts})

def post_detail(request, slug):
    """Create page with post content"""
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'my_blog/post_detail.html', context={'post': post})