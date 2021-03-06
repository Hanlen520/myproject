# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-14 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20181114_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='project_name',
            field=models.ForeignKey(default='',
                                    on_delete=django.db.models.deletion.CASCADE
                                    , related_name='case_project_name',
                                    to='myapp.Ym'),
        ),
        migrations.AlterField(
            model_name='case_suite',
            name='status',
            field=models.CharField(default='\u672a\u5f00\u59cb', max_length=50),
        ),
    ]
