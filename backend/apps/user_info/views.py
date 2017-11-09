#-*- coding: utf-8 -*-

from rest_framework import viewsets

from apps.user_info.models import UserInfo
from apps.user_info.serializers import UserInfoSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
