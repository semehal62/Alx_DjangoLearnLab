from .models import Author, Book, Library, Librarian

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.get(author=author)

books = Book.objects.all().values()

librarian = Library.objects.get(name=library_name).librarian