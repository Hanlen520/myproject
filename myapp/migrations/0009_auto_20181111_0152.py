# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-11 01:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20181110_0608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='project_name',
        ),
        migrations.AddField(
            model_name='case',
            name='project_name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='case_project_name', to='myapp.Ym'),
        ),
    ]
