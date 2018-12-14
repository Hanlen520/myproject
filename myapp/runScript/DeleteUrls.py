# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from myapp.serializers import AddUrls
from myapp.models import Ym
from rest_framework.views import APIView
from rest_framework.response import Response
import logging


class DeleteUrls(APIView):
    queryset = Ym.objects.all().filter(isdelete=False)
    serializer_class = AddUrls

    def put(self, request):

        data = request.data
        for i in data["ids"]:
            try:
                Ym.objects.filter(ym_id=i).update(isdelete=True)
                return Response("{'code': 200, 'message': '成功'}")

            except Exception as e:
                logging.exception(e)
                return Response(e)
