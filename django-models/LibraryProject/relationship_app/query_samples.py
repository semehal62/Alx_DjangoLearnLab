from .models import Author, Book, Library, Librarian


# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    return books_by_author


# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    return books_in_library


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    return librarian
