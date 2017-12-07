#-*- coding: utf-8 -*-

import os
import re
from django.conf import settings
from django.db import models

from django.contrib.auth.models import User

def validator_title(value):
    pattern = r"^[\s\S]*[\"#\$%&\'\(\)\*\+/:;<=>?@\[\\\]\^_`\{\|\}~]"
    if re.match(pattern, value):
        return False
    return True


class Thesis(models.Model):
    SUBJ_TYPES = (
        ('CE', u'通信工程'),
        ('IS', u'信息与计算科学'),
    )

    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thesis') # 指导老师
    stu_name = models.CharField(max_length=20, null=False, blank=False) # 学生姓名
    stu_num = models.IntegerField(null=False, blank=False, unique=True) # 学生学号
    stu_subj = models.CharField(max_length=2, null=False, blank=False, choices=SUBJ_TYPES) # 学生专业
    graduation_year = models.IntegerField(null=False, blank=False) # 毕业年份
    title = models.CharField(max_length=100, null=False, blank=False, validators=[validator_title]) # 论文题目
    created_date = models.DateField(auto_now_add=True) # 创建时间
    last_update_time = models.DateTimeField(auto_now=True) # 最近更新时间

    @property
    def subject(self):
        return self.get_stu_subj_display()

    @property
    def file_structure(self):
        return os.path.join(self.stu_subj, str(self.graduation_year), self.instructor.user_info.username_cn,
                            '{}_{}'.format(self.stu_num, self.stu_name))

    @property
    def file_path(self):
        return os.path.join(settings.BASE_DIR, 'thesis', self.file_structure)
