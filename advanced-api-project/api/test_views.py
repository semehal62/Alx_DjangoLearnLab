from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
import datetime

# import user
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client.login(username='testuser', password='testpass')
        


        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )
        self.list_url = reverse('book-list')  # /books/
        self.detail_url = reverse('book-detail', args=[self.book.id])  # /books/<id>/
        self.create_url = reverse('book-create')  # /books/create/
        self.update_url = reverse('book-update', args=[self.book.id])  # /books/<id>/update/
        self.delete_url = reverse('book-delete', args=[self.book.id])  # /books/<id>/delete/

    # ---------- CRUD TESTS ----------
    def test_create_book(self):
        data = {
            "title": "Animal Farm",
            "publication_year": 1945,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.last().title, "Animal Farm")

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "1984")

    def test_update_book(self):
        data = {
            "title": "Nineteen Eighty-Four",
            "publication_year": 1949,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # ---------- FILTERING TEST ----------
    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {'publication_year': 1949})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book['publication_year'] == 1949 for book in response.data))

    # ---------- SEARCH TEST ----------
    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any('1984' in book['title'] for book in response.data))

    # ---------- ORDERING TEST ----------
    def test_order_books_by_title_descending(self):
        Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get(self.list_url, {'ordering': '-title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles, reverse=True))

    # ---------- VALIDATION TEST ----------
    def test_future_publication_year_fails(self):
        next_year = datetime.date.today().year + 1
        data = {
            "title": "Future Book",
            "publication_year": next_year,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Publication year cannot be in the future.', str(response.data))
