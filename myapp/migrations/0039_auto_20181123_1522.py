# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-23 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0038_auto_20181118_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='request_data',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
