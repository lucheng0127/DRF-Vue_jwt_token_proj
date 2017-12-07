#-*- coding: utf-8 -*-

from rest_framework import serializers

from apps.user_info.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = UserInfo
        fields = ['id', 'user', 'nickname', 'username_cn', 'job', 'role']
        read_only_fields = ['role', 'job']
