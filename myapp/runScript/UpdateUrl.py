# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 更新域名
class UpdateUrl(generics.RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)
