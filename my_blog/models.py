from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_posted = models.DateField(default=timezone.now)
    # foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # relationships many to many
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        """generate unike url path for post"""
        return reverse('post_detail', kwargs={'slug': self.slug})


class Tag(models.Model):
    tag = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.tag}'

    def get_absolute_url(self):
        """generate unike url path for tags"""
        return reverse('tag_detail', kwargs={'slug': self.slug})


