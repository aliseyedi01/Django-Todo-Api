from rest_framework.permissions import BasePermission


class IsAuthenticatedAndOwner(BasePermission):

    def has_permission(self, request, view):
        # Allow only authenticated users to perform any CRUD operations.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read permissions to any authenticated user.
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True

        # Only allow the owner of the object to perform write (update, delete) operations.
        return obj.user == request.user
