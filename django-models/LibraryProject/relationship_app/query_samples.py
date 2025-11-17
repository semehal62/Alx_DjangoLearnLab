books_by_author = Book.object.get(author = author_name)
books = Book.object.all().values()
librarian = library.object.get(name = library_name)
