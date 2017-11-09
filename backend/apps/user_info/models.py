#-*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User


class UserInfo(models.Model):
    ROLE_TYPE = (
        ('teacher', u'老师'),
        ('subject_leader', u'专业领导'),
        ('college_leader', u'学院领导'),
        ('admin', u'管理员'),
    )

    user = models.OneToOneField(User, related_name='user_info', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30, null=False, blank=False) # 老师姓名全拼加数字
    username_cn = models.CharField(max_length=30, null=False, blank=False, unique=True) # 中文名
    job = models.CharField(max_length=100, null=True, blank=True, default='') # 工作职位
    role = models.CharField(max_length=15, null=False, blank=False, default='teacher') # 权限
