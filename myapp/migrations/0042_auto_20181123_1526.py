# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-23 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0041_auto_20181123_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_bz',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='case',
            name='request_data',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
