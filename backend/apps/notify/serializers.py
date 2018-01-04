#-*- coding: utf-8 -*-

from rest_framework import serializers

from apps.notify.models import Notify


class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = ['id', 'title', 'body', 'remark', 'created_by', 'created_by_cn', 'created_date']
        read_only_fields = ['id', 'created_by', 'created_by_cn', 'created_date']
