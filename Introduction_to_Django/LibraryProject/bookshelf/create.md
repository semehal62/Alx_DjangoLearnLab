


new_book = Book.objects.create(title = “1984”, author = “George Orwell”, publication_year = "1949")
new_book.save()

# expected out put   [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]>
