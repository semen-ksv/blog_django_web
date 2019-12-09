from django.shortcuts import render


def main_index(request):
    """Create main index page url('/')"""
    if request.method == 'GET':
        return render(request, 'django_blog/main_index.html')
