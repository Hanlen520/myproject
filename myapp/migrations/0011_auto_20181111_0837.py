# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-11 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20181111_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_suite',
            name='project_name',
            field=models.ManyToManyField(blank=True, default='', to='myapp.Ym'),
        ),
        migrations.AlterField(
            model_name='case_suite',
            name='suite_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]