# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-25 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0048_auto_20181125_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='ym',
            name='result',
            field=models.CharField(default='', max_length=1000),
        ),
    ]