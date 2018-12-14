# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym


# 删除域名
class DeleteUrl(generics.RetrieveDestroyAPIView):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def perform_destroy(self, instance):
        Ym.objects.filter(ym_id=instance.ym_id).update(isdelete=True)
