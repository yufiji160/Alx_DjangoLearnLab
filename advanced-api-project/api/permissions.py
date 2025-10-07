from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only the author of the book can edit/delete it.
    Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
