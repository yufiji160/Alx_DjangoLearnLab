from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post

class TagSearchTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='pass')
        p1 = Post.objects.create(title='Django tips', content='Use django-taggit for tags', author=user)
        p2 = Post.objects.create(title='Python tricks', content='test content here', author=user)
        p1.tags.add('django', 'tutorial')
        p2.tags.add('python')

    def test_search_by_keyword(self):
        resp = self.client.get('/search/?q=django')
        self.assertContains(resp, 'Django tips')
    
    def test_search_by_tag(self):
        resp = self.client.get('/search/?q=python')
        self.assertContains(resp, 'Python tricks')

    def test_posts_by_tag_view(self):
        resp = self.client.get('/tags/django/')
        self.assertContains(resp, 'Django tips')