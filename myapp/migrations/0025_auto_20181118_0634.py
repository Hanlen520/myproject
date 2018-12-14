# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-18 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20181117_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_suite',
            name='suite_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='ym',
            name='project_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='ym',
            name='url_name',
            field=models.CharField(max_length=50),
        ),
    ]
