from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Пермишен для модераторов
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Moderator").exists()


class IsOwner(permissions.BasePermission):
    """
    Пермишен для владельца лекций и курсов
    """
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False
