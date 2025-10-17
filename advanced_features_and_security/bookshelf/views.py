from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from .models import Book
from .forms import SafeSearchForm, BookForm
from django.db.models import Q
from django.utils.html import escape

@require_http_methods(["GET"])
def book_list(request):
    """
    Secure book list with a search form. Uses Django forms to validate input
    and the ORM (parameterized queries) to avoid SQL injection.
    """
    form = SafeSearchForm(request.GET or None)
    books = Book.objects.all()

    if form.is_valid():
        q = form.cleaned_data.get("q")
        if q:
            books = books.filter(Q(title__icontains=q) | Q(author__icontains=q))

    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})

@require_http_methods(["GET", "POST"])
def add_book(request):
    """
    Example view that safely handles user input via ModelForm.
    ModelForm + ORM avoid direct SQL interpolation.
    """
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/form_example.html", {"form": form})
