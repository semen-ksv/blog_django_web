from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utilities import ObjectDetailMixin
from .forms import TagForm

def blog_posts_list(request):
    """Create main page in blog page"""
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'my_blog/blog_post_list.html', context={'posts': posts})

# def post_detail(request, slug):
#     """Create page with post content"""
#     if request.method == 'GET':
#         post = Post.objects.get(slug__iexact=slug)
#         return render(request, 'my_blog/post_detail.html', context={'post': post})


# def tag_detail(request, slug):
#     tag = Tag.objects.get(slug__iexact=slug)
#     return render(request, 'my_blog/tag_detail.html', context={'tag': tag})

class PostDetail(ObjectDetailMixin, View):
    # def get(self, request, slug):
    #     """Create page with post content"""
    #     # post = Post.objects.get(slug__iexact=slug)
    #     post = get_object_or_404(Post, slug__iexact=slug)
    #     return render(request, 'my_blog/post_detail.html', context={'post': post})
    model = Post
    template = 'my_blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'my_blog/tag_detail.html', context={'tag': tag})
    model = Tag
    template = 'my_blog/tag_detail.html'


class TagCreate(View):
    def get(self, request):
        """form for creating Tags"""
        form = TagForm()
        return render(request, 'my_blog/tag_create.html', context={'form': form})



def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'my_blog/tag_list.html', context={'tags': tags})