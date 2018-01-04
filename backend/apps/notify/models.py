#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Notify(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default='')  # 通知标题
    body = models.TextField(default='')  # 内容
    remark = models.CharField(max_length=200, null=True, blank=True, default='')  # 备注
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notify')  # 发布人
    created_date = models.DateField(auto_now_add=True)  # 发布时间

    @property
    def created_by_cn(self):
        return self.created_by.user_info.username_cn
