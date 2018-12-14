# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-13 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20181111_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case_suite',
            name='project_name',
        ),
        migrations.AddField(
            model_name='case_suite',
            name='project_name',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='myapp.Ym'),
        ),
    ]
