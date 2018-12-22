# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
import re
from myapp.models import Case, Case_suite


class RunCaseSuites(APIView):

    def get_case(self):
        # 查询要运行的套件信息
        data = Case_suite.objects.get(suite_id=i)
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type":
                                          "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            t = requests.get(url, json=request_data, headers=headers,
                             verify=False)
            if t.status_code == 200:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())

                # return Response(t.json(), status=status.HTTP_200_OK,
                #                 headers=headers)
                # return Response(t)
            else:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='失败')
                # return Response(t.json(), status=t.status_code,
                #                 headers=headers)
        except Exception as e:
            return Response(e)

    def post_case(self):
        data = Case_suite.objects.get(suite_id=i)
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type":
                                          "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            t = requests.post(url, json=eval(request_data),
                              headers=headers, verify=False)
            if t.status_code == 201:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())
                # return Response(t.json(),
                #                 status=status.HTTP_201_CREATED,
                #                 headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='失败')
                # return Response(t.json(), status=t.status_code,
                #                 headers=headers)
        except Exception as e:
            return Response(e)

    def put_case(self):
        data = Case_suite.objects.get(suite_id=i)
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type":
                                          "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            t = requests.put(url, json=eval(request_data),
                             headers=headers, verify=False)
            if t.status_code == 200:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='成功')
                Case.objects.filter(isdelete=False,
                                    case_name=data.case.case_name).update(
                    result=t.json())
                # return Response(t.json(), status=status.HTTP_200_OK,
                #                 headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='失败')
                # return Response(t.json(), status=t.status_code,
                #                 headers=headers)
        except Exception as e:
            return Response(e)

    def delete_case(self):
        data = Case_suite.objects.get(suite_id=i)
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers

            headers = data.headers
            headers = eval(headers)
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            token = requests.post("http://127.0.0.1:8000/api-auth/",
                                  json={"username": "zhengxq1",
                                        "password": "zxq111111"},
                                  headers={
                                      "Content-Type":
                                          "application/json; charset=utf-8"})
            headers["Authorization"] = "Jwt " + token.json()['token']
            t = requests.delete(url, json=eval(request_data),
                                headers=headers, verify=False)
            if t.status_code == 204:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='成功')
                # return Response(t.json(),
                #                 status=status.HTTP_204_NO_CONTENT,
                #                 headers=headers)
            else:
                Case_suite.objects.filter(
                    suite_id=i).update(
                    status='失败')
                # return Response(t.json(), status=t.status_code,
                #                 headers=headers)
        except Exception as e:
            return Response(e)

    def post(self, request):
        global serializers
        serializers = request.data
        # 循环获取到的接口列表
        # 获取到的id列表
        global i
        for i in serializers["ids"]:
            print(i)
            data = Case_suite.objects.get(suite_id=i)
            # 查询测试套件下对应的测试用例信息
            data1 = Case.objects.filter(isdelete=False).get(
                case_name=data.case.case_name)
            try:
                # 获取headers

                headers = data.headers
                headers = eval(headers)
                # # 获取请求地址
                url = data.yuming.url_name + data1.url
                # # 获取请求数据
                request_data = data1.request_data
                # # 获取请求类型
                request_type = data1.request_type
                # # 获取token信息
                token = requests.post("http://127.0.0.1:8000/api-auth/",
                                      json={"username": "zhengxq1",
                                            "password": "zxq111111"},
                                      headers={
                                          "Content-Type":
                                              "application/json; charset=utf-8"})
                headers["Authorization"] = "Jwt " + token.json()['token']
                # 请求参数未填写情况下赋值空值
                # if request_data == '':
                #     request_data = {}
                # get请求处理
                logging.debug('不调用其他接口返回数据')
                if data1.case_bz == "":
                    if request_type == 'get':
                        self.get_case()
                        # return Response(results.data)
                    # post请求处理
                    if request_type == 'post':
                        self.post_case()
                        # return Response(results.data)
                    # put请求处理
                    if request_type == 'put':
                        self.put_case()
                        # return Response(results.data)
                    # delete请求处理
                    if request_type == 'delete':
                        self.delete_case()
                        # return Response(results.data)
                if data1.case_bz != "":
                    # 遍历要返回数据的列表id
                    for key in eval(data1.case_bz):
                        try:
                            # 通过正则找到要替换的字段，进行替换
                            res = re.compile('(\[\w*_?\w*\])')
                            # 查找到带【】的参数
                            t1 = res.search(url)
                            body_res = res.findall(request_data)
                            if t1 and len(body_res) > 0:
                                # 将【】替换为空
                                t1 = t1.group(0)
                                t2 = t1.replace('[', '')
                                t2 = t2.replace(']', '')
                                url_pattern = (
                                    eval(Case.objects.get(case_id=key).result)[
                                        t2])
                                new_data = request_data
                                for body in body_res:
                                    new_body = body.replace('[', '')
                                    new_body = str(new_body).replace(']', '')
                                    new_body = eval(
                                        Case.objects.get(case_id=key).result)[
                                        new_body]
                                    new_data = new_data.replace(body,
                                                                '\'' + str(
                                                                    new_body) +
                                                                '\'')
                                # 查询上一个接口返回的数据，替换url中的参数

                                new_url = url.replace(t1, str(url_pattern))
                                if request_type == 'put':
                                    t = requests.put(new_url,
                                                     json=eval(new_data),
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'post':
                                    t = requests.post(new_url,
                                                      json=eval(new_data),
                                                      headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #
                                        #             status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'get':
                                    t = requests.get(new_url,
                                                     json=new_data,
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #             status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)

                                if request_type == 'delete':
                                    t = requests.delete(new_url,
                                                        json=new_data,
                                                        headers=headers)
                                    if t.status_code == 204:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update()
                                        # return Response(
                                        #     status=status.HTTP_204_NO_CONTENT,
                                        #     headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(
                                        #     status=t.status_code,
                                        #     headers=headers)
                            elif t1 and len(body_res) == 0:
                                t1 = t1.group(0)
                                t2 = t1.replace('[', '')
                                t2 = t2.replace(']', '')
                                url_pattern = (
                                    eval(Case.objects.get(case_id=key).result)[
                                        t2])
                                # 查询上一个接口返回的数据，替换url中的参数

                                new_url = url.replace(t1, str(url_pattern))
                                if request_type == 'put':
                                    t = requests.put(new_url,
                                                     json=eval(request_data),
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'post':
                                    t = requests.post(new_url,
                                                      json=eval(request_data),
                                                      headers=headers)
                                    if t.status_code == 201:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'get':
                                    t = requests.get(new_url,
                                                     json=request_data,
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)

                                if request_type == 'delete':
                                    t = requests.delete(new_url,
                                                        json=request_data,
                                                        headers=headers)
                                    if t.status_code == 204:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=
                                            data.case.case_name).update()
                                        # return Response(
                                        #     status=status.HTTP_204_NO_CONTENT,
                                        #     headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(
                                        #     status=t.status_code,
                                        #     headers=headers)
                            if not t1 and len(body_res) > 0:
                                # 将【】替换为空
                                new_data = request_data
                                for body in body_res:
                                    new_body = body.replace('[', '')
                                    new_body = str(new_body).replace(']', '')
                                    new_body = eval(
                                        Case.objects.get(case_id=key).result)[
                                        new_body]
                                    new_data = new_data.replace(body,
                                                                '\'' + str(
                                                                    new_body) +
                                                                '\'')
                                # 查询上一个接口返回的数据，替换url中的参数
                                if request_type == 'put':
                                    t = requests.put(url,
                                                     json=eval(new_data),
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'post':
                                    t = requests.post(url,
                                                      json=eval(new_data),
                                                      headers=headers)
                                    if t.status_code == 201:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=data.case.case_name
                                        ).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)
                                if request_type == 'get':
                                    t = requests.get(url,
                                                     json=new_data,
                                                     headers=headers)
                                    if t.status_code == 200:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=data.case.case_name
                                        ).update(
                                            result=t.json())
                                        # return Response(t.json(),
                                        #                 status=status.HTTP_200_OK,
                                        #                 headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(t.json(),
                                        #                 status=t.status_code,
                                        #                 headers=headers)

                                if request_type == 'delete':
                                    t = requests.delete(url,
                                                        json=new_data,
                                                        headers=headers)
                                    if t.status_code == 204:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='成功')
                                        Case.objects.filter(
                                            isdelete=False,
                                            case_name=data.case.case_name
                                        ).update()
                                        # return Response(
                                        #     status=status.HTTP_204_NO_CONTENT,
                                        #     headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=i).update(
                                            status='失败')
                                        # return Response(
                                        #     status=t.status_code,
                                        #     headers=headers)
                        except Exception as e:
                            return Response(e)

            except Exception as e:
                return Response(e)
        t = {'code': 200, 'message': '成功'}
        return Response(t)
