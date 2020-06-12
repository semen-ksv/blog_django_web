from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Post, Tag
from .utilities import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, CommentForm


# def blog_posts_list(request):
#     """Create main page in blog page"""
#     if request.method == 'GET':
#         posts = Post.objects.all()
#         return render(request, 'my_blog/blog_post_list.html', context={'posts': posts})
def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    return render(request, 'my_blog/blog_post_list.html', context={'posts': posts})


class PostsList(ListView):
    """Show all post on Article page"""
    model = Post
    template_name = 'my_blog/blog_post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8



class AuthorPostsList(ListView):
    model = Post
    template_name = 'my_blog/author_post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

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


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, CreateView):
    redirect_field_name = 'login'
    raise_exception = True
    # def get(self, request):
    #     """form for creating Tags"""
    #     form = PostForm()
    #     return render(request, 'my_blog/post_create.html', context={'form': form})
    #
    # def post(self, request):
    #     """read data from forms"""
    #     bound_form = PostForm(request.POST)  # связаная форма
    #
    #     if bound_form.is_valid():
    #         new_post = bound_form.save()
    #         return redirect(new_post)
    #     return render(request, 'my_blog/post_create.html', context={'form': bound_form})
    # model = Post
    form_model = PostForm
    template = 'my_blog/post_create.html'

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    model = Post
    form = PostForm
    template = 'my_blog/post_update.html'


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    raise_exception = True
    model = Post
    template = 'my_blog/post_delete.html'
    redirect_url = 'blog_home'


class TagDetail(ObjectDetailMixin, View):
    # def get(self, request, slug):
    #     # tag = Tag.objects.get(slug__iexact=slug)
    #     tag = get_object_or_404(Tag, slug__iexact=slug)
    #     return render(request, 'my_blog/tag_detail.html', context={'tag': tag})
    model = Tag
    template = 'my_blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    raise_exception = True
    # def get(self, request):
    #     """form for creating Tags"""
    #     form = TagForm()
    #     return render(request, 'my_blog/tag_create.html', context={'form': form})
    #
    # def post(self, request):
    #     """read data from forms"""
    #     bound_form = TagForm(request.POST)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'my_blog/tag_create.html', context={'form': bound_form})
    form_model = TagForm
    template = 'my_blog/tag_create.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    raise_exception = True
    # """modification existing tags"""
    # def get(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(instance=tag)
    #     return render(request, 'my_blog/tag_update.html', context={'form': bound_form, 'tag': tag})
    #
    # def post(self, request, slug):
    #     tag = Tag.objects.get(slug__iexact=slug)
    #     bound_form = TagForm(request.POST, instance=tag)
    #
    #     if bound_form.is_valid():
    #         new_tag = bound_form.save()
    #         return redirect(new_tag)
    #     return render(request, 'my_blog/tag_update.html', context={'form': bound_form, 'tag': tag})
    model = Tag
    form = TagForm
    template = 'my_blog/tag_update.html'


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    raise_exception = True
    model = Tag
    template = 'my_blog/tag_delete.html'
    redirect_url = 'tags_list'


# def tags_list(request):
#     tags = Tag.objects.all()
#     return render(request, 'my_blog/tag_list.html', context={'tags': tags})

class TagsList(ListView):
    model = Tag
    template_name = 'my_blog/tag_list.html'
    context_object_name = 'tags'
    ordering = ['tag']

class AddComment(LoginRequiredMixin, View):
    """Add new comments for post"""
    raise_exception = True

    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = post
            form.user = request.user
            form.save()
        return redirect(post.get_absolute_url())