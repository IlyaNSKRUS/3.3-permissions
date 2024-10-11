from rest_framework.permissions import BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return request.user == obj.creator or bool(request.user and request.user.is_staff)