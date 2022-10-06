from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Check if user is profile Owner or not.
    """

    def has_object_permission(self, request, view, obj):
        return (obj == request.user)
