# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 查询测试套件列表
class CaseSuiteList(generics.ListAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
