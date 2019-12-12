#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Django's command-line utility for administrative tasks."""
import os
import sys

# __author__ == 'Semen Kotsuryuruba'
__version__ = "0.0.1"

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# virtualenv venv
# sourse venv/bin/activate
# django-admin startprogect
# manage.py startapp django_blog
# py manage.py runserver
# py manage.py migrate
# py manage.py createsuperuser
# admin admin
# py manage.py makemigrations
# py manage.py migrate
# p2 = Post.objects.create(title='Second blog post', slug='second_blog_post', body='Second post content Second post content Second post content Second post content Second post content Second post content', author=user)