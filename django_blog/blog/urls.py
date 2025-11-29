from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    ListView, 
    CreateView, 
    UpdateView, 
    DetailView, 
    DeleteView, 
    BlogDetailView, 
    CommentCreateView, 
    CommentUpdateView, 
    CommentDeleteView, 
    search_posts,
    PostByTagListView,
    ProfileView,
)

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('post/', ListView.as_view(), name='posts'),
    path('posts/search/', search_posts, name='search_posts'),
    path('post/new/', CreateView.as_view(), name='new-post'),
    path('post/<int:pk>/detail/', DetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeleteView.as_view(), name='post-delete'),

    # Post-related URLs
    path('posts/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    
    # Comment URLs (updated to match requested patterns)
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    
    path('posts/tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post_by_tag'),
]