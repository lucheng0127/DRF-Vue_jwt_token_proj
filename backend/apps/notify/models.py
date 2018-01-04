#-*- coding: utf-8 -*-
import re

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


def validator_data(value):
    pattern = r"^[\s\S]*[\"#\$%&\'\(\)\*\+/:;<=>?@\[\\\]\^_`\{\|\}~]"
    if re.match(pattern, value):
        raise ValidationError('含有特殊字符！')
    return True


class Notify(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default='', validators=[validator_data])  # 通知标题
    body = models.TextField(default='', validators=[validator_data])  # 内容
    remark = models.CharField(max_length=200, null=True, blank=True, default='', validators=[validator_data])  # 备注
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notify')  # 发布人
    created_date = models.DateField(auto_now_add=True)  # 发布时间

    @property
    def created_by_cn(self):
        return self.created_by.user_info.username_cn
