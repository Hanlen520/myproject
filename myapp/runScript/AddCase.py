# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class AddCase(generics.ListCreateAPIView):
    # 标记需要进行jwt验证
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case.objects.filter(isdelete=False)
    serializer_class = Cases
