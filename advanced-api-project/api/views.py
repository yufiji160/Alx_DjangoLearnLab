from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
        print("✅ A new book was created successfully!")

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['message'] = "Book created successfully!"
        return response


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
        print("✏️ Book details updated successfully!")

    def put(self, request, *args, **kwargs):
        response = super().put(request, *args, **kwargs)
        response.data['message'] = "Book updated successfully!"
        return response
