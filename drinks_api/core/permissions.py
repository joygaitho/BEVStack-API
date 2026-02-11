from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
   Allows read-only access to unauthenticated users.
   Write access is restricted to admin users.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Read-only access for everyone
        
        return (
            request.user and
            request.user.is_authenticated and
            request.user.is_staff
        )  