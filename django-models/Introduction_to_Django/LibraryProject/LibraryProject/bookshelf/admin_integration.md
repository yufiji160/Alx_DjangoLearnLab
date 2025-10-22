# Django Admin Integration for Book Model

## Overview
This document describes how to integrate and customize the Book model with the Django admin interface.

## Steps

1. **Register the Book model:**
   In `bookshelf/admin.py`, import and register the Book model.

   ```python
   from django.contrib import admin
   from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
