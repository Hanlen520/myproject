# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-17 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20181117_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case_suite',
            name='bz',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
