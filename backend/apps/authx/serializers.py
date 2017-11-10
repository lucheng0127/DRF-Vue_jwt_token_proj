#-*- coding: utf-8 -*-

from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    user_info = serializers.HyperlinkedIdentityField(view_name='user-info-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_info']


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
