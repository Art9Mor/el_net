from rest_framework.permissions import BasePermission


class IsActiveEmployee(BasePermission):
    """
    Allows access only to active employees.
    """
    def has_permission(self, request, view):
        return request.user.is_active
