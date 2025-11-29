from rest_framework import serializers
from .models import Author, Book
import datetime # imported module to get access to the current year

# Used to serialize the 'Book' model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Use field-level validation for publication_year
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            # Raise the exception to halt validation
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Use the actual class, not a string representation
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        # Include the nested 'books' serializer in the fields
        fields = ['id', 'name', 'books']
