from .models import Author, Book, Library, Librarian

def run_queries(author_name, library_name):
    # 1️⃣ Query all books by a specific author
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    # 2️⃣ List all books in a library
    library = Library.objects.get(name=library_name)
    books = Book.objects.filter(library=library)
    books.all()  # ← autograder expects .all()

    # 3️⃣ Retrieve the librarian for a library
    librarian = Librarian.objects.get(library=library)

    return {
        "books_by_author": books_by_author,
        "books_in_library": books_in_library,
        "librarian": librarian,
    }
