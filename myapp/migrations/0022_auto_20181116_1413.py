# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-16 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_auto_20181116_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_bz',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
