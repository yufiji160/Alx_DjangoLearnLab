from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class UserAuthTests(TestCase):
    def test_register_creates_user(self):
        response = self.client.post(reverse('blog:register'), {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, reverse('blog:profile'))

    def test_login_valid_user(self):
        User.objects.create_user(username='tester', password='pass12345')
        response = self.client.post(reverse('login'), {
            'username': 'tester',
            'password': 'pass12345'
        })
        self.assertEqual(response.status_code, 302)

    def test_profile_requires_login(self):
        response = self.client.get(reverse('blog:profile'))
        self.assertRedirects(response, '/login/?next=/profile/')
