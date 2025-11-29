# accounts/urls.py
from django.urls import path, include

app_name = 'accounts' # Important for namespacing

urlpatterns = [
    # Django's built-in authentication URLs
    # These provide views for login, logout, password change/reset etc.
    # You might have a custom login view in your accounts/views.py for specific functionality.
    # For now, we'll just include Django's defaults.
    path('', include('django.contrib.auth.urls')),
]
