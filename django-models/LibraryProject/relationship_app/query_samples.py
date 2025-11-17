from .models import Author, Book, Library, Librarian

author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

books = Book.objects.all().values()
books.all()
librarian = Library.objects.get(name=library_name).librarian
librarian = Librarian.objects.get(library = name_librarian)