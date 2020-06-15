from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Post, Tag
from .utilities import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, CommentForm



def search(request):
    # form to search for articles
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()
    return render(request, 'my_blog/search_post_list.html', context={'posts': posts})


class PostsList(ListView):
    """Show all post on Article page"""

    model = Post
    template_name = 'my_blog/blog_post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 8



class AuthorPostsList(ListView):
    """Create page with post for one author"""

    model = Post
    template_name = 'my_blog/author_post_list.html'
    context_object_name = 'posts'
    paginate_by = 7

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetail(ObjectDetailMixin, View):
    """Create page with post content"""

    model = Post
    template = 'my_blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, CreateView):
    """form for creating article in Post model"""

    redirect_field_name = 'login'
    raise_exception = True
    form_model = PostForm
    template = 'my_blog/post_create.html'


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """form for updating article in Post model"""

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
    """Create page with post for one tag"""

    model = Tag
    template = 'my_blog/tag_detail.html'
    context_object_name = 'tags'
    paginate_by = 7



class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    """form for creating Tags"""

    raise_exception = True
    form_model = TagForm
    template = 'my_blog/tag_create.html'


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    """modification existing tags"""

    raise_exception = True
    model = Tag
    form = TagForm
    template = 'my_blog/tag_update.html'


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):

    raise_exception = True
    model = Tag
    template = 'my_blog/tag_delete.html'
    redirect_url = 'tags_list'


class TagsList(ListView):
    """page show all tags"""

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