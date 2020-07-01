from django.test import TestCase
from django.contrib.auth.models import User
from time import time
from my_blog.models import generate_slug, Post, Comment

class TestModels(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            username='Sem'
        )
        self.post = Post()
        self.post.title = 'Test News',
        self.post.body = 'Some testing text',
        self.post.author = self.user
        self.post.post_img = 'post-image1.jpg'
        self.post.save()

    def test_post_fields(self):
        record_post = Post.objects.get(pk=self.post.pk)
        self.assertEqual(record_post, self.post)

    def test_generate_slug(self):
        self.assertEqual(generate_slug('Test News'), f'test-news_{str(int(time()))}')

    def test_comment_fields(self):
        comment = Comment()
        comment.user = self.user
        comment.body = 'Good comment'
        comment.post = self.post
        comment.save()

        record_comment = Comment.objects.get(pk=comment.pk)
        self.assertEqual(record_comment, comment)
