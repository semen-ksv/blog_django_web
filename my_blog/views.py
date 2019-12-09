from django.shortcuts import render

def blog_posts_list(request):
    """Create main page in blog page"""
    # if request.method == 'GET':
    my_name = "Sem"
    return render(request, 'my_blog/blog_post_list.html', context={'name': my_name})
