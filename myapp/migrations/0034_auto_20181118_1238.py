# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-18 12:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0033_auto_20181118_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='login',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]