# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-10 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20181110_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='project_name',
            field=models.ManyToManyField(default='',
                                         related_name='case_project_name',
                                         to='myapp.Ym'),
        ),
    ]
