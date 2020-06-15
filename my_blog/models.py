from PIL import Image
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def generate_slug(title):
    new_slug = slugify(title, allow_unicode=True)
    return new_slug + '_' + str(int(time()))


class Post(models.Model):
    """Model for posts in blog"""
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    body = RichTextUploadingField(blank=True, db_index=True)
    date_posted = models.DateField(default=timezone.now)
    post_img = models.ImageField(null=True, blank=True, upload_to='post_images/', verbose_name='image')
    # foreign keys
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # relationships many to many
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """generate unique url path for post"""
        return reverse('post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        """:return url path for tags in update form"""
        return reverse('post_update', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        """generate and save new slug for new title"""
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)

        img = Image.open(self.post_img.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.post_img.path)

    @property
    def get_comments(self):
        """ get comments from Comment model fof Post"""
        return self.comments.all().order_by('-date_comment')

    @property
    def comment_count(self):
        """count all comments for self Post"""
        return Comment.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_comment = models.DateField(default=timezone.now)
    body = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.user.username}'


class Tag(models.Model):
    """Model for Tags"""
    tag = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.tag

    def get_update_url(self):
        """:return url path for tags in update form"""
        return reverse('tag_update', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        """generate unique url path for tags"""
        return reverse('tag_detail', kwargs={'slug': self.slug})
