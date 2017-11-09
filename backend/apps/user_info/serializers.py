#-*- coding: utf-8 -*-

from rest_framework import serializers

from apps.user_info.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInfo
        fields = ['nickname', 'username_cn', 'job', 'role']
        read_only_fields = ['role']
