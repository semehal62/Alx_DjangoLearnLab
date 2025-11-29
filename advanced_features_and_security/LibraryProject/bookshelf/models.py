from django.db import models
from django.contrib.auth.models import AbstractUser

# Importing user manager Model
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    class Meta:
        permissions = [
            ("can_view", "Can View Book"),
            ("can_create", "Can Create Book"),
            ("can_edit", "Can Edit Book"),
            ("can_delete", "Can Delete Book"),
        ]

#permissions

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(
        null=True, 
        blank=True
    )
    profile_photo = models.ImageField(
        upload_to='profile_photos/', 
        null=True, 
        blank=True
    )


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('date_of_birth', None)  # Default for custom field
        extra_fields.setdefault('profile_photo', None)  # Default for custom field
        return super().create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('date_of_birth', None)  # Optional for superuser
        extra_fields.setdefault('profile_photo', None)  # Optional for superuser
        return super().create_superuser(username, email, password, **extra_fields)