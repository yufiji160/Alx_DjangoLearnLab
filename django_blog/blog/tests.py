from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='author', password='pass')
        self.other = User.objects.create_user(username='other', password='pass')
        self.post = Post.objects.create(title='Test', content='content', author=self.user)

    def test_list_view(self):
        resp = self.client.get(reverse('blog:post-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test')

    def test_detail_view(self):
        resp = self.client.get(reverse('blog:post-detail', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'content')

    def test_create_requires_login(self):
        resp = self.client.get(reverse('blog:post-create'))
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='author', password='pass')
        resp = self.client.get(reverse('blog:post-create'))
        self.assertEqual(resp.status_code, 200)

    def test_update_author_only(self):
        self.client.login(username='other', password='pass')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        #
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='author', password='pass')
        resp = self.client.get(reverse('blog:post-update', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_delete_author_only(self):
        self.client.login(username='other', password='pass')
        resp = self.client.get(reverse('blog:post-delete', kwargs={'pk': self.post.pk}))
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='author', password='pass')
        resp = self.client.get(reverse('blog:post-delete', kwargs={'pk': self.post.pk}))
        self.assertEqual(resp.status_code, 200)

    def test_create_post(self):
        self.client.login(username='author', password='pass')
        resp = self.client.post(reverse('blog:post-create'), {'title': 'New', 'content': 'b', 'published': True})
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New').exists())

