# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from rest_framework import generics
from myapp.models import Ym
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 删除域名
class DeleteUrl(generics.RetrieveDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def perform_destroy(self, instance):
        Ym.objects.filter(ym_id=instance.ym_id).update(isdelete=True)
