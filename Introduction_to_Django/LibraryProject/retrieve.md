from bookshelf.models import Book

# Retrieve all books
Book.objects.all()
# Expected output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
