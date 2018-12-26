# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 更新测试用例套件
class UpdateCaseSuite(generics.RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case_suite.objects.filter(isdelete=False)
    serializer_class = CaseSuites
