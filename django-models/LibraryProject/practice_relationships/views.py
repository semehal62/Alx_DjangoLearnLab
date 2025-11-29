# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\practice_relationships\views.py

# Existing imports...
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView # <--- Make sure TemplateView is imported
from django.shortcuts import render

# Add these new imports for permission handling
from django.contrib.auth.mixins import PermissionRequiredMixin # <--- Make sure this is imported


# Your existing SignUpView class...
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

# Your other existing views (if any)

# --- THIS IS THE CRUCIAL PART: ENSURE THIS CLASS IS EXACTLY AS BELOW ---
class LibrarianDashboardView(PermissionRequiredMixin, TemplateView):
    permission_required = 'bookshelf.view_book'
    template_name = 'practice_relationships/librarian_dashboard.html'
    login_url = 'login'
    # raise_exception = True # Optional: Uncomment for 403 instead of redirect
# --- END NEW PROTECTED VIEW ---
