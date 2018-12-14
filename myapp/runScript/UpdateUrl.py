# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym


# 更新域名
class UpdateUrl(generics.RetrieveUpdateAPIView):
    serializer_class = AddUrls
    queryset = Ym.objects.all().filter(isdelete=False)
