# -*- coding:utf-8 -*-
from rest_framework import generics
from myapp.models import Case_suite
from myapp.serializers import CaseSuites


# 删除测试套件
class DeleteCaseSuite(generics.RetrieveDestroyAPIView):
    queryset = Case_suite.objects.all().filter(isdelete=False)
    serializer_class = CaseSuites

    def perform_destroy(self, instance):
        Case_suite.objects.filter(suite_id=instance.suite_id).update(
            isdelete=True)
