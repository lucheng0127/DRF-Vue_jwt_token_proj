# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='role',
            field=models.CharField(choices=[('teacher', '老师'), ('subject_leader', '专业领导'), ('college_leader', '学院领导'), ('admin', '管理员')], default='teacher', max_length=15),
        ),
    ]
