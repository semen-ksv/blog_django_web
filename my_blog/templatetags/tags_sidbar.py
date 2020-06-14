from django import template
from my_blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('my_blog/reacent_posts_temp.html')
def get_recent(cnt=3):
    posts = Post.objects.order_by('-date_posted')[:cnt]
    return {'posts': posts}


@register.inclusion_tag('my_blog/all_tags.html')
def get_all_tags():
    tags = Tag.objects.all()
    return {'tags': tags}
