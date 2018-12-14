# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym


# 新增域名
class AddUrl1(generics.ListCreateAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)
