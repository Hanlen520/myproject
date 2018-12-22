# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Login(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True, unique=True,
                                default='')
    password = models.CharField(max_length=100, blank=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Ym(models.Model):
    ym_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50, blank=False)
    url_name = models.CharField(max_length=50, blank=False)
    bz = models.TextField(max_length=100, blank=True)
    result = models.CharField(max_length=1000, blank=False, default='')
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return self.project_name


class Case(models.Model):
    case_id = models.AutoField(primary_key=True)
    case_name = models.CharField(max_length=50, blank=False)
    project_name = models.ForeignKey(Ym, default='', on_delete=models.CASCADE,
                                     blank=False,
                                     related_name='case_project_name',
                                     error_messages={"blank": "项目名称不能为空"})
    request_type = models.CharField(max_length=50, blank=False)
    url = models.CharField(max_length=100, blank=False)
    case_bz = models.CharField(max_length=200, blank=True, default='')
    request_data = models.CharField(max_length=200, blank=True)
    isdelete = models.BooleanField(default=False)
    expected_result = models.CharField(max_length=500, blank=False, default='')
    result = models.CharField(max_length=500, default='', blank=True)
    assert_value = models.CharField(max_length=50, default='', blank=False)
    invoking_login = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.case_name


class Case_suite(models.Model):
    suite_id = models.AutoField(primary_key=True)
    suite_name = models.CharField(max_length=50, blank=False)
    project_name = models.ForeignKey(Ym, default='', blank=False,
                                     related_name='suite_project_name',
                                     on_delete=models.CASCADE)
    yuming = models.ForeignKey(Ym, default='', blank=False,
                               related_name='suite_yuming',
                               on_delete=models.CASCADE)
    headers = models.CharField(max_length=200, default='', blank=False)
    case = models.ForeignKey(Case, max_length=50, default='',
                             related_name="suite_case_name",
                             on_delete=models.CASCADE,
                             blank=False)
    bz = models.CharField(max_length=200, default='', blank=True)
    isdelete = models.BooleanField(default=False, blank=False)
    status = models.CharField(max_length=50, default='未开始', blank=False)
    result = models.CharField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.suite_name
