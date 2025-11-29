from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book  

#import the forms 

from .forms import ExampleForm

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Fetch all books from the database
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def search_books(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        # Securely filter books using the ORM
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})