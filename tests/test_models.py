from django.test import TestCase
from time import time
from my_blog.models import *

class TestModels(TestCase):

    # def setUp(self) -> None:
    #     self.post1 = Post.objects.create(
    #         title='Test News',
    #         body='Some testing text',
    #     )

    def test_generate_slug(self):
        self.assertEqual(generate_slug('Test News'), f'test-news_{str(int(time()))}')