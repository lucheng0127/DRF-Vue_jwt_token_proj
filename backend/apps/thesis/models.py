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


class ThesisLog(models.Model):
    '''
    论文材料上传记录
    '''
    FILE_CHOICE = (
        ('MANDATE', u'01任务书'),
        ('SCHEDULE1', u'02指导计划表(教师)'),
        ('SCHEDULE2', u'03指导计划表(学生)'),
        ('PROPOSAL', u'04开题报告'),
        ('CHECKLIST', u'05中期检查表'),
        ('PPT1', u'06中期检答辩PPT'),
        ('DEFENCE', u'07答辩申请表'),
        ('ADVICE', u'08导教师意见'),
        ('REVIEW', u'09评阅意见'),
        ('THESIS', u'10论文'),
        ('PPT2', u'11答辩PPT'),
        ('SCORE', u'12成绩登记表'),
        ('SOURCECODE', u'13源代码'),
    )

    thesis = models.ForeignKey(Thesis, on_delete=models.CASCADE, related_name='thesis_log') # 对应的毕业论文
    last_upload_time = models.DateTimeField(auto_now=True) # 最近一次上传时间
    created_date = models.DateField(auto_now_add=True) # 第一次上传时间
    file = models.CharField(max_length=10, choices=FILE_CHOICE, null=False, blank=False) # 材料名称
    upload_times = models.IntegerField(default=0) # 提交次数

    @property
    def upload_to_path(self):
        return self.thesis.file_path

    @property
    def filename_cn(self):
        return self.get_file_display()
