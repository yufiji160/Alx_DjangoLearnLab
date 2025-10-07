from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListCreateAPIView):
    """
    Supports:
    - GET: list books
    - POST: create a new book
    - Filtering, searching, ordering
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'publication_year']  
    search_fields = ['title'] 
    ordering_fields = ['publication_year']


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Supports:
    - GET: retrieve one
    - PUT/PATCH: update
    - DELETE: remove
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
