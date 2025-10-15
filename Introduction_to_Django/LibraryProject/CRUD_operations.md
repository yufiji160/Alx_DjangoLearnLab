# CRUD Operations

## Create
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984 by George Orwell (1949)>

## Retrieve
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell (1949)>]>

## Update
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.all()
<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>

## Delete
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
>>> Book.objects.all()
<QuerySet []>
