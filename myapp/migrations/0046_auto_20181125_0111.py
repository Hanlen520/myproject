# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-25 01:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_login_isdelete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='login',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
