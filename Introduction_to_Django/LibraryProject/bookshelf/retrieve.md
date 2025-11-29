from bookshelf.models import Book
new_book = Book.objects.get(publication_date=1984)