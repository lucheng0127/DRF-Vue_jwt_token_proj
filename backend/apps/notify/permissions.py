#-*- coding: utf-8 -*-

from rest_framework import permissions


class IsDirectorOrReadOnly(permissions.BasePermission):
    '''
    admin or director can post, delete. put
    teacher can get
    '''
    def has_permission(self, request, view):
        allow_role_list = ['admin', 'subject_leader', 'college_leader']
        if request.user.is_superuser or request.user.user_info.role in allow_role_list:
            return True

        elif request.method in permissions.SAFE_METHODS:
            return True

        return False
