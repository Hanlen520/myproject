# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from myapp.models import Ym
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


class DeleteUrls(APIView):
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def put(self, request):

        data = request.data
        print(data)
        for i in data["ids"]:
            try:
                Ym.objects.filter(ym_id=i).update(isdelete=True)
            except Exception as e:
                logging.exception(e)
        return Response("{'code': 200, 'message': '成功'}")
