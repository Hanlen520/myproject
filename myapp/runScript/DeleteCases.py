# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import Cases
from myapp.models import Case
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# 批量删除测试用例
class DeleteCases(APIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Case.objects.all().filter(isdelete=False)
    serializer_class = Cases

    def put(self, request):
        return_message = {'code': 200, 'message': '成功'}

        data = request.data
        for i in data["ids"]:
            try:
                Case.objects.filter(case_id=i).update(isdelete=True)

            except Exception as e:
                logging.exception(e)
        return Response(return_message)
