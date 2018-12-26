# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 更新测试用例信息
class UpdateCase(generics.RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases
