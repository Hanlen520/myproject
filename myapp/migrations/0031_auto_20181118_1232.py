# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-18 12:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0030_auto_20181118_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
    ]
