# Create Operation

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

**Commands:**
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year