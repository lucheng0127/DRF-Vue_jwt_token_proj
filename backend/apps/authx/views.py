#-*- coding: utf-8 -*-

import re

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route

from django.contrib.auth.models import User

from apps.authx.serializers import UserSerializer, UserCreateSerializer
from apps.authx.permissions import IsSuperuserOrOwnerOrReadOnly


def validator_username(value):
    pattern = r"^[\s\S]*[\"#\$%&\'\(\)\*\+/:;<=>?@\[\\\]\^_`\{\|\}~]"
    if re.match(pattern, value):
        return False
    return True


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsSuperuserOrOwnerOrReadOnly,)

    def create(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        data = request.data
        if not validator_username(data['username']):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if len(data['password']) < 8:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserCreateSerializer(data=data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.data)
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    @detail_route(methods=['POST'])
    def set_passwd(self, request, pk=None):
        user = User.objects.get(pk=pk)
        if not (user == request.user or request.user.is_superuser):
            return Response({'msg': u'只有本人和管理员可以修改密码'}, status=status.HTTP_403_FORBIDDEN)
        data = request.data
        if len(data['password']) < 8:
            return Response({'msg': u'密码至少8位'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user.set_password(data['password'])
            user.save()
            return Response({'msg': u'设置密码成功'}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
