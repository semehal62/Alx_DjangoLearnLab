from bookshelf.models import Book
new_book.delete()
Book.objects.all().values()
# expected output ->  (1, {'bookshelf.Book': 1})

