from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('list/', BookList.as_view(), name='book-list'),  # Optional: keep your original endpoint
    path('', include(router.urls)),  # Includes all ViewSet routes
]