# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework import generics
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


# 删除测试用例
class DeleteCase(generics.RetrieveDestroyAPIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case.objects.all().filter(isdelete=False)
    serializer_class = Cases

    def perform_destroy(self, instance):
        Case.objects.filter(case_id=instance.case_id).update(isdelete=True)
