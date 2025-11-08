
>>> new_book = Book(title = 'Introduction to django', author = 'willium s. vincent', publication_year = '2019')
>>> new_book.save()
>>> books_by_author = Book.objects.filter(author = 'willium s. vincent')
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Introduction to django', 'author': 'willium s. vincent', 'publication_year': 2019}]>
>>> new_book.title = "Django to everyone"
>>> new_book.save()
>>> Book.objects.all().values()
<QuerySet [{'id': 1, 'title': 'Django to everyone', 'author': 'willium s. vincent', 'publication_year': 2019}]>
>>> new_book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all().values()
<QuerySet []>
>>>
