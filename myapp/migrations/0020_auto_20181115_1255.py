# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-15 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20181114_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_name',
            field=models.CharField(error_messages={'unique': '\u7528'
                                                             '\u4f8b\u540d'
                                                             '\u79f0\u5df2'
                                                             '\u5b58\u5728'},
                                   max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='case_suite',
            name='suite_name',
            field=models.CharField(blank=True, error_messages={'unique':
                                                                   '\u5957\u4ef6'
                                                                   '\u540d'
                                                                   '\u79f0'
                                                                   '\u5df2'
                                                                   '\u5b58'
                                                                   '\u5728'},
                                   max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ym',
            name='project_name',
            field=models.CharField(error_messages={'null':
                                                       '\u9879\u76ee\u540d'
                                                       '\u4e0d\u80fd'
                                                       '\u4e3a\u7a7a',
                                                   'unique':
                                                       '\u9879\u76ee'
                                                       '\u5df2\u5b58\u5728'},
                                   max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ym',
            name='url_name',
            field=models.CharField(error_messages={'unique':
                                                       '\u57df\u540d'
                                                       '\u5df2\u5b58'
                                                       '\u5728'},
                                   max_length=50, unique=True),
        ),
    ]
