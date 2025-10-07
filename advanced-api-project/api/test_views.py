from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class TestBookAPI(APITestCase):
    def setUp(self):
        #user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        #authors
        self.author_a = Author.objects.create(name="Author A")
        self.author_b = Author.objects.create(name="Author B")

        #Author instances
        self.book1 = Book.objects.create(title="Book One", author=self.author_a, publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author=self.author_b, publication_year=2021)

        #API
        self.books_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse('book-detail', args=[pk])

    def test_list_books(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.books_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "New Book",
            "author": self.author_a.id,
            "publication_year": 2022
        }
        response = self.client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book(self):
        """Test updating an existing book"""
        url = self.book_detail_url(self.book1.id)
        data = {
            "title": "Updated Book One",
            "author": self.author_a.id,
            "publication_year": 2020
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        """Test deleting a book"""
        url = self.book_detail_url(self.book2.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(self.books_url, {'author': self.author_a.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author_a.id)

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get(self.books_url, {'search': 'Book One'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('Book One' in b['title'] for b in response.data))

    def test_order_books_by_year(self):
        """Test ordering books by publication year"""
        response = self.client.get(self.books_url, {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data[0]['publication_year'], response.data[1]['publication_year'])

    def test_unauthenticated_access(self):
        """Test that unauthenticated users cannot create books"""
        client = APIClient()
        data = {"title": "Forbidden Book", "author": self.author_a.id, "publication_year": 2023}
        response = client.post(self.books_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
