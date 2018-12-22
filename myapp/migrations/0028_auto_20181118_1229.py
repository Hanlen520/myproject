# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-18 12:29
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('myapp', '0027_auto_20181118_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='name',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(
                error_messages={'unique':
                                    'A user with that username already exists.'}
                ,
                help_text=
                'Required. 150 characters or fewer. Letters, '
                'digits and @/./+/-/_ only.',
                max_length=150, unique=True, validators=[
                    django.contrib.auth.validators.ASCIIUsernameValidator()],
                verbose_name='username'),
        ),
    ]
