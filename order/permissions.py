from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    """
    Check if user is Customer or not.
    """

    def has_object_permission(self, request, view, obj):
        return obj.customer == request.user


class IsExecutor(permissions.BasePermission):
    """
    Check if user is Customer or not.
    """

    def has_object_permission(self, request, view, obj):
        return obj.executor == request.user


class IsCustomerOrExecutor(permissions.BasePermission):
    """
    Check if user is Customer or not.
    """

    def has_object_permission(self, request, view, obj):
        return (obj.executor == request.user or obj.customer == request.user)
