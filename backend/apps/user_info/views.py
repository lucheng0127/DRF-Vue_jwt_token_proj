#-*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.user_info.models import UserInfo
from apps.user_info.serializers import UserInfoSerializer
from apps.user_info.permissions import IsAdminOrOwner


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = (IsAdminOrOwner, IsAuthenticated)

    def get_queryset(self):
        if self.request.user.user_info.role == 'admin':
            return UserInfo.objects.all()
        return UserInfo.objects.filter(user=self.request.user)
