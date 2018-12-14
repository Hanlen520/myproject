# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites


# 增加测试套件
class AddCaseSuite(generics.ListCreateAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
