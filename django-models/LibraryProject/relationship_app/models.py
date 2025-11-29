# relationship_app/models.py

from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from django.db.models.signals import post_save # Import signal for automatic profile creation
from django.dispatch import receiver # Import receiver decorator for signals

# 1. Define Author first, as it has no dependencies on other custom models
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 2. Define Library next.
#    It needs to refer to 'Book' using a string because Book is defined later.
class Library(models.Model):
    name = models.CharField(max_length=100)
    # Use 'Book' as a string because the Book model is defined *after* Library in this file.
    books = models.ManyToManyField('Book', related_name='libraries')

    def __str__(self):
        return self.name

# 3. Define Book.
#    It can now refer to Author and Library directly because they are defined above.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField(null=True, blank=True)
    # Library is defined above, so direct reference is fine here.
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        # Define custom permissions
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title

# 4. Define Librarian.
#    It can refer to Library directly because Library is defined above.
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    # OneToOneField: A librarian is responsible for one specific library, and a library has one librarian.
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name

# 5. Define UserProfile (depends on User, which is imported)
#    This should be last among your custom models.
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username}'s Profile ({self.role})"

# 6. Signals (assuming you kept them in models.py from previous instructions,
#    though they are usually in a separate signals.py and imported in apps.py's ready method)
#    If you have signals in relationship_app/signals.py, you don't need these here.
#    If you *don't* have relationship_app/signals.py, then you MUST have these here
#    and ensure relationship_app/apps.py is configured to load them.

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     # Check if userprofile exists before trying to save it, to avoid errors
#     # for users created before UserProfile model existed
#     if hasattr(instance, 'userprofile'):
#         instance.userprofile.save()
