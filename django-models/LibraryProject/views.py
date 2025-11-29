# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\practice_relationships\views.py

# Existing imports...
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView # <--- ADD TemplateView here
from django.shortcuts import render

# Add these new imports for permission handling
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator


# Your existing SignUpView class...
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Add your existing views if any (e.g., bookshelf views)

# --- ADD THIS NEW PROTECTED VIEW ---
class LibrarianDashboardView(PermissionRequiredMixin, TemplateView):
    # The permission required to access this view.
    # Format: 'app_label.permission_codename'
    permission_required = 'bookshelf.view_book' # Use a permission assigned to Librarians group
    template_name = 'practice_relationships/librarian_dashboard.html'
    login_url = 'login' # Redirect to login if not authenticated
    # raise_exception = True # Optional: If True, raises 403 Forbidden instead of redirecting if logged in but no permission

# Alternatively, for a function-based view:
# @login_required
# @user_passes_test(lambda u: u.groups.filter(name='Librarians').exists() or u.has_perm('bookshelf.view_book'))
# def librarian_dashboard_func(request):
#     return render(request, 'practice_relationships/librarian_dashboard.html')
# --- END NEW PROTECTED VIEW ---
