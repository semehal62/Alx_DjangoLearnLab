# C:\Users\user\Alx_DjangoLearnLab\django-models\LibraryProject\practice_relationships\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Commented out problematic paths for now:
    # path('hello-relationships/', views.hello_relationships_view, name='hello_relationships'),
    # path('companies/', views.company_list_view, name='company_list'),
    # path('companies/<int:pk>/', views.company_detail_view, name='company_detail'),

    # This is the only one we need active for current testing:
    path('librarian_dashboard/', views.LibrarianDashboardView.as_view(), name='librarian_dashboard'),
]
