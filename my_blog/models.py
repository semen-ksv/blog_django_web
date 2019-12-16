from django.db import models
from django.http import request
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def generate_slug(title):
    new_slug = slugify(title, allow_unicode=True)
    return new_slug + '_' + str(int(time()))


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_posted = models.DateField(default=timezone.now)
    # foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # relationships many to many
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """generate unike url path for post"""
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        """:return url path for tags in update form"""
        return reverse('post_update', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """generate and save new slug for new title"""
        if not self.id:
            self.slug = generate_slug(self.title)
        # if not self.author:
        #     self.author = User.username
        super().save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.tag

    def get_update_url(self):
        """:return url path for tags in update form"""
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        """generate unike url path for tags"""
        return reverse('tag_detail', kwargs={'slug': self.slug})
