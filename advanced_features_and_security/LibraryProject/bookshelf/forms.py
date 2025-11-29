
from django import forms
from django.utils import timezone
from .models import CustomUser

class UserSearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search by username or email'})
    )

    def clean_query(self):
        query = self.cleaned_data.get('query', '')
        if query and len(query) < 3:
            raise forms.ValidationError("Search query must be at least 3 characters long.")
        return query

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'profile_photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get('date_of_birth')
        if dob and dob > timezone.now().date():
            raise forms.ValidationError("Date of birth cannot be in the future.")
        return dob

    def clean_profile_photo(self):
        photo = self.cleaned_data.get('profile_photo')
        if photo:
            if not photo.content_type.startswith('image/'):
                raise forms.ValidationError("Only image files are allowed.")
            if photo.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Profile photo must be smaller than 5MB.")
        return photo

# ExampleForm - a simple example form
class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Email must be from the domain 'example.com'.")
        return email
