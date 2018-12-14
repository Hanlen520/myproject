# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites


# 查询测试套件列表
class CaseSuiteList(generics.ListAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
