from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import Post, Tag
from .utilities import ObjectDetailMixin
from .forms import TagForm, PostForm


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

class PostCreate(View):
    def get(self, request):
        """form for creating Tags"""
        form = PostForm()
        return render(request, 'my_blog/post_create.html', context={'form': form})

    def post(self, request):
        """read data from forms"""
        bound_form = PostForm(request.POST)  # связаная форма

        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'my_blog/post_create.html', context={'form': bound_form})




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

    def post(self, request):
        """read data from forms"""
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'my_blog/tag_create.html', context={'form': bound_form})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'my_blog/tag_list.html', context={'tags': tags})
