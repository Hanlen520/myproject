# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import CaseSuites
from myapp.models import Case_suite
from rest_framework.views import APIView
import logging
from rest_framework.response import Response


# 批量删除测试套件
class DeleteCaseSuites(APIView):
    queryset = Case_suite.objects.all().filter(isdelete=False)
    serializer_class = CaseSuites

    def put(self, request):
        t = {'code': 200, 'message': '成功'}
        data = request.data
        for i in data["ids"]:
            try:
                Case_suite.objects.filter(suite_id=i).update(isdelete=True)
            except Exception as e:
                logging.exception(e)
        return Response(t)
