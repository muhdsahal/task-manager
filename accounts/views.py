from rest_framework import permissions

class CustomIsAuthenticated(permissions.BasePermission):
    """
    Allows access only to authenticated users.
    Custom behavior can be added here.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated
        if request.user and request.user.is_authenticated:
            # You can add extra logic here if needed
            # Example: Only allow users with active status
            if hasattr(request.user, 'is_active') and not request.user.is_active:
                return False
            return True

        return False

    def message(self):
        # Custom error message
        return "You must be logged in to access this resource."

class IsSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'superadmin'


class IsAdminOrSuperAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ('admin', 'superadmin')


class IsTaskOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    - SuperAdmin → can access all tasks.
    - Admin → can access tasks of users assigned to them.
    - Normal User → can only access their own tasks.
    """
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False

        # SuperAdmin can do anything
        if request.user.role == 'superadmin':
            return True

        # Admin: check if task belongs to one of their users
        if request.user.role == 'admin':
            return obj.assigned_to.assigned_admin_id == request.user.id

        # Otherwise, user must be the task owner
        return obj.assigned_to == request.user
