from django.db import models

class Author(models.Model):
    """
    Author model:
    Represents a writer who can have multiple books.
    One-to-many relationship: One author -> Many books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    Each book is linked to an Author using a ForeignKey.
    Fields:
        - title: Title of the book.
        - publication_year: Year the book was published.
        - author: The author (one-to-many relationship).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
