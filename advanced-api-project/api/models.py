from django.db import models

# Define the Author model to represent authors
class Author(models.Model):
<<<<<<< HEAD
    """
    Author model:
    - name: author's full name
    - Relationship: an Author can have many Books (one-to-many).
    """
=======
>>>>>>> 5bd438abef634e8d5612d7baf748ecd4f07275c6
    name = models.CharField(max_length=200)

    # magic method to have the string representation of the name field
    def __str__(self):
        return self.name


# Define the Book model to represent books
class Book(models.Model):
<<<<<<< HEAD
    """ 
    Book model:
     - title; title of the book.
     - publication_year: integer year the book was published.
     - author: ForeignKey to Author (related_name = 'books').
     """
    title = models.CharField(max_length=255)
=======
    title = models.CharField(max_length=200)
>>>>>>> 5bd438abef634e8d5612d7baf748ecd4f07275c6
    publication_year = models.IntegerField()
    
    # Foreign key field used to represent 'one-to-many' relationship between the author and books.
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    # magic method to have the string representation of the title field
    def __str__(self):
        return self.title
