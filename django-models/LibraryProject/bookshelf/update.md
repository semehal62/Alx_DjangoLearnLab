from bookshelf.models import Book

book = Book.objects.get(publication_date=1984)
book.title = "Nineteen Eighty-Four" 