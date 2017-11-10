#-*- coding: utf-8 -*-

from rest_framework import permissions


class IsSuperuserOrOwnerOrReadOnly(permissions.BasePermission):
    '''
    superuser can create user, delete user, owner can modify user info, logged user can read
    '''
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        elif request.method in permissions.SAFE_METHODS:
            return True

        elif request.method in ['PUT', 'PATCH']:
            return obj == request.user
