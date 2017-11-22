#-*- coding: utf-8 -*-

from rest_framework import serializers

from apps.thesis.models import Thesis

class ThesisSerializer(serializers.ModelSerializer):
    instructor = serializers.ReadOnlyField(source='instructor.user_info.username_cn')
    # stu_subj = serializers.SerializerMethodField()

    class Meta:
        model = Thesis
        fields = ['id', 'instructor', 'stu_name', 'stu_num', 'stu_subj', 'subject',
                  'graduation_year', 'title', 'created_date', 'last_update_time',
                  'file_structure']
        read_only_fields = ['id', 'subject', 'file_structure']

    # def get_stu_subj(self, obj):
    #     return obj.get_stu_subj_display()
