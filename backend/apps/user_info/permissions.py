#-*- coding: utf-8 -*-

from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.user_info.role == 'admin':
            return True

        elif obj.user == request.user:
            return True

        return False
