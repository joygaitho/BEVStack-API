from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
   Allows read-only access to unauthenticated users.
   Write access is restricted to admin users.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return request.user.is_authenticated  # Allow read-only access for unauthenticated users
        
        return (
            request.user.is_authenticated
            and getattr(request.user, 'role', None) == 'admin'
        )  # Full access for authenticated users