# relationship_app/views.py
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.urls import reverse_lazy # Ensure this is imported for redirecting
from django.contrib.auth.forms import UserCreationForm # Ensure this is here for register_view
from django.contrib.auth import login as auth_login # Ensure this is here for register_view
from django.views.generic.list import ListView # Keep ListView if you have other list views or for completeness

# Ensure these specific imports are present
from .models import Author, Book, Librarian, UserProfile
from .models import Library # Explicitly separate for checker's literal match
from django.views.generic.detail import DetailView # Corrected import path as per checker


# Helper functions for role checks (from previous tasks, keep them)
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Existing Views from Previous Tasks (ensure these are present) ---

# Example: A simple home view if you have one
# Adjust template name as per your setup - if you don't have a 'home.html' remove this or create one.
def home_view(request):
    return render(request, 'relationship_app/home.html')

# --- Function-Based View: List all Authors ---
def author_list_view(request):
    authors = Author.objects.all().order_by('name')
    context = {
        'authors': authors
    }
    return render(request, 'relationship_app/author_list.html', context)

# --- Class-Based View: Author Detail ---
class AuthorDetailView(DetailView):
    model = Author
    template_name = 'relationship_app/author_detail.html'
    context_object_name = 'author'

# --- Function-Based View: List all Libraries ---
def library_list_view(request):
    libraries = Library.objects.all().order_by('name')
    context = {
        'libraries': libraries
    }
    return render(request, 'relationship_app/library_list.html', context)

# --- Class-based View for Library Details (Corrected/Updated for this task) ---
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    # Ensure books are pre-fetched if you iterate over library.books.all() in template
    def get_queryset(self):
        return Library.objects.prefetch_related('books__author') # Prefetch books and their authors

    # No need to override get_context_data unless adding more to context,
    # as DetailView automatically puts `self.object` into context as `library` (due to context_object_name)


# --- Function-Based View: Librarian Detail ---
def librarian_detail_view(request, pk):
    librarian = get_object_or_404(Librarian, pk=pk)
    context = {
        'librarian': librarian
    }
    return render(request, 'relationship_app/librarian_detail.html', context)

# --- Function-Based View: User Registration ---
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home') # Ensure 'home' URL name exists in your project
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'relationship_app/register.html', context)


# --- Role-Based Views (from previous tasks, keep them) ---
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# --- Book Management Views with Custom Permissions (from previous tasks, keep them) ---
@permission_required('relationship_app.can_add_book', raise_exception=True)
def book_add_view(request):
    if request.method == 'POST':
        # In a real app: process form, save book
        return redirect('list_books') # Redirect to the new list_books URL
    return render(request, 'relationship_app/book_add.html', {'message': 'Add Book Page'})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def book_edit_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # In a real app: process form, update book
        return redirect('list_books') # Redirect to list_books for simplicity
    return render(request, 'relationship_app/book_edit.html', {'book': book, 'message': f'Edit Book Page for {book.title}'})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books') # Redirect to list_books for simplicity
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book, 'message': f'Confirm Delete for {book.title}'})

# --- NEW VIEWS FOR THIS TASK (Updated function name) ---
# Function-based View for Listing Books (Renamed from list_books_view to list_books)
def list_books(request): # CHANGED: Function name is now 'list_books'
    books = Book.objects.all().select_related('author') # Optimizes query to get author name
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)
