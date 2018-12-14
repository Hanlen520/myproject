# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites


# 更新测试用例套件
class UpdateCaseSuite(generics.RetrieveUpdateAPIView):
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
