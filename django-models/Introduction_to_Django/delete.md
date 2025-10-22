# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
# Output: (1, {'bookshelf.Book': 1})

from bookshelf.models import Book
Book.objects.all()
# Output: <QuerySet []>

---



You can concatenate all four markdown files:

```bash
cat create.md retrieve.md update.md delete.md > CRUD_operations.md
