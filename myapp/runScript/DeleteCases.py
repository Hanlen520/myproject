# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework.views import APIView
import logging
from rest_framework.response import Response


# 批量删除测试用例
class DeleteCases(APIView):
    queryset = Case.objects.all().filter(isdelete=False)
    serializer_class = Cases

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}
        error_message = {"code": 0, 'message': '用例已被删除'}
        list1 = []

        data = request.data
        for i in data["ids"]:
            try:
                Case.objects.filter(case_id=i).update(isdelete=True)

            except Exception as e:
                logging.exception(e)
        return Response(return_message)
