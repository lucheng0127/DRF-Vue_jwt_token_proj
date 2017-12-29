#-*- coding: utf-8 -*-

from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.user_info.role == 'admin':
            return True

        elif obj.instructor == request.user:
            return True

        elif request.method in permissions.SAFE_METHODS:
            if request.user.user_info.role == 'subject_leader':
                return obj.stu_subj == request.user.user_info.job.split('_',)[0]
            return False

        return False


def can_download(user, obj):
    if user.is_superuser or user.user_info.role == 'admin':
        return True

    elif obj.thesis.instructor == user:
        return True

    elif user.user_info.role == 'subject_leader':
        return obj.thesis.stu_subj == user.user_info.job.split('_', )[0]

    return False
