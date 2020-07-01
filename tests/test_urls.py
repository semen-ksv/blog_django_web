from django.test import SimpleTestCase
from django.urls import reverse, resolve
from my_blog.views import *

# py manage.py test tests


class TestUrls(SimpleTestCase):

    def test_blog_home_url(self):
        url = reverse('blog_home')
        self.assertEqual(resolve(url).func.view_class, PostsList)

    def test_search_home_url(self):
        url = reverse('search_home')
        self.assertEqual(resolve(url).func, search)

    def test_author_post_url(self):
        url = reverse('author_post', args=['author_username',])
        self.assertEqual(resolve(url).func.view_class, AuthorPostsList)

    def test_post_create_url(self):
        url = reverse('post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreate)

    def test_post_detail_url(self):
        url = reverse('post_detail', args=['post_slug',])
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_post_comment_url(self):
        url = reverse('post_comment', args=[12,])
        self.assertEqual(resolve(url).func.view_class, AddComment)

    def test_post_update_url(self):
        url = reverse('post_update', args=['post_slug',])
        self.assertEqual(resolve(url).func.view_class, PostUpdate)

    def test_post_delete_url(self):
        url = reverse('post_delete', args=['post_slug',])
        self.assertEqual(resolve(url).func.view_class, PostDelete)

    def test_tags_list_url(self):
        url = reverse('tags_list')
        self.assertEqual(resolve(url).func.view_class, TagsList)

    def test_tag_create_url(self):
        url = reverse('tag_create')
        self.assertEqual(resolve(url).func.view_class, TagCreate)

    def test_tag_detail_url(self):
        url = reverse('tag_detail', args=['tag_slug',])
        self.assertEqual(resolve(url).func.view_class, TagDetail)

    def test_tag_update_url(self):
        url = reverse('tag_update', args=['tag_slug',])
        self.assertEqual(resolve(url).func.view_class, TagUpdate)

    def test_tag_delete_url(self):
        url = reverse('tag_delete', args=['tag_slug',])
        self.assertEqual(resolve(url).func.view_class, TagDelete)

    def test_photography_url(self):
        url = reverse('photography')
        self.assertEqual(resolve(url).func.view_class, AllPhotography)