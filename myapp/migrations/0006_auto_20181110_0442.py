# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-10 04:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20181110_0438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='case',
            name='project_name',
        ),
        migrations.RemoveField(
            model_name='case_suite',
            name='project_name',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Case',
        ),
        migrations.DeleteModel(
            name='Case_suite',
        ),
        migrations.DeleteModel(
            name='Ym',
        ),
    ]