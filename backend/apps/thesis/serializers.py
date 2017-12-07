#-*- coding: utf-8 -*-

from rest_framework import serializers

from apps.thesis.models import Thesis, ThesisLog


class ThesisLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThesisLog
        fields = ['id', 'thesis', 'last_update_time', 'created_date', 'file', 'upload_times']
        read_only_fields = ['id', 'thesis', 'last_update_time', 'created_date', 'file', 'upload_times']


class ThesisSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.user_info.username_cn')
    thesis_log = ThesisLogSerializer(many=True, read_only=True)

    class Meta:
        model = Thesis
        fields = ['id', 'instructor', 'stu_name', 'stu_num', 'stu_subj', 'subject',
                  'graduation_year', 'title', 'created_date', 'last_update_time',
                  'file_structure', 'thesis_log']
        read_only_fields = ['id', 'subject', 'file_structure']

