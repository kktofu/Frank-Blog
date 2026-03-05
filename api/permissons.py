from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, User):
            return obj == request.user

        author = getattr(obj, 'author', None) or getattr(obj, 'comment_author', None)

        return author == request.user
