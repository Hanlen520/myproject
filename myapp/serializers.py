# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Login
from .models import Ym, Case, Case_suite
from rest_framework.validators import UniqueValidator


class Login1(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = "__all__"


class AddUrls(serializers.ModelSerializer):
    project_name = serializers.CharField(max_length=50,
                                         validators=[UniqueValidator(
                                             queryset=Ym.objects.filter(
                                                 isdelete=False),
                                             message=("项目名已存在"))],
                                         error_messages={"blank": "项目名称不能为空"})
    url_name = serializers.CharField(max_length=50,
                                     validators=[UniqueValidator(
                                         queryset=Ym.objects.all().filter(
                                             isdelete=False),
                                         message=("域名已存在"))], required=True,
                                     error_messages={"blank": "域名不能为空"})
    bz = serializers.CharField(allow_blank=True, max_length=100, required=False,
                               style={'base_template': 'textarea.html'})
    ym_id = serializers.IntegerField(read_only=True)
    isdelete = serializers.BooleanField(default=False)

    class Meta:
        model = Ym
        fields = ("project_name", "url_name", "bz", "ym_id", "isdelete")


class Cases(serializers.ModelSerializer):
    case_id = serializers.IntegerField(read_only=True)
    project_name = serializers.SlugRelatedField(
        queryset=Ym.objects.filter(isdelete=False), slug_field="project_name",
        required=True,
        error_messages={"null": "项目名称不能为空"})
    case_name = serializers.CharField(max_length=50,
                                      validators=[
                                          UniqueValidator(
                                              queryset=Case.objects.filter(
                                                  isdelete=False), message=(
                                                  "用例名已存在"
                                              ))], required=True,
                                      error_messages={"blank": "用例名称不能为空"})
    url = serializers.CharField(max_length=100, required=True,
                                error_messages={"blank": "url不能为空"})
    case_bz = serializers.CharField(max_length=200)
    request_type = serializers.CharField(max_length=50, required=True,
                                         error_messages={"blank": "请求类型不能为空"})
    request_data = serializers.CharField(max_length=200, required=False,
                                         allow_blank=True)

    class Meta:
        model = Case
        fields = ("case_id", "project_name", "case_name", "url", "case_bz",
                  "request_type", "request_data")


class Case_list(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class CaseSuites(serializers.ModelSerializer):
    yuming = serializers.SlugRelatedField(
        queryset=Ym.objects.filter(isdelete=False), slug_field="url_name",
        required=True,
        error_messages={"null": "域名不能为空"})
    case = serializers.SlugRelatedField(
        queryset=Case.objects.filter(isdelete=False), slug_field="case_name",
        required=True,
        error_messages={"null": "用例名不能为空"})
    project_name = serializers.SlugRelatedField(
        queryset=Ym.objects.filter(isdelete=False), slug_field="project_name",
        required=True,
        error_messages={"null": "项目名不能为空"})
    bz = serializers.CharField(max_length=200, required=False, allow_blank=True)
    suite_name = serializers.CharField(max_length=50,
                                       validators=[
                                           UniqueValidator(
                                               queryset=Case_suite.objects.filter(
                                                   isdelete=False),
                                               message=("套件名已存在"))],
                                       required=True,
                                       error_messages={"blank": "套件名不能为空"})
    headers = serializers.CharField(max_length=200, required=True,
                                    error_messages={"blank": "头文件不能为空"})
    suite_id = serializers.IntegerField(read_only=True)
    status = serializers.CharField(max_length=50, required=False)

    class Meta:
        model = Case_suite
        fields = (
            'yuming', "case", "project_name", "bz", "suite_name", "headers",
            "suite_id", "status")


class LoginIn(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ("user_id", "username", "password")
