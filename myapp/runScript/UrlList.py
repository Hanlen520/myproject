# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym


# 查询所有域名信息
class UrlList(generics.ListAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)
