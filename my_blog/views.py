from django.shortcuts import render

# Create your views here.
def blog_posts_list(request):
    if request.method == 'GET':
        return render(request, 'my_blog/blog_post_list.html')