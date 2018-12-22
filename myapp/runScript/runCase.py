# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from rest_framework.views import APIView
import logging
from rest_framework.response import Response
from rest_framework import status
import re
from myapp.models import Case, Case_suite, Ym


class Quest(APIView):
    # 封装登陆接口
    def login(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        request_data = eval(Case.objects.get(
            case_id=data1.invoking_login).request_data)
        login_url = Case.objects.get(case_id=data1.invoking_login).url
        login_project_name = Case.objects.get(
            case_id=data1.invoking_login).project_name
        login_yuming = Ym.objects.get(project_name=login_project_name,
                                      isdelete=False).url_name
        url = login_yuming + login_url
        headers = eval(data.headers)
        if data1.invoking_login != '':
            Case.objects.filter(isdelete=False).get(
                case_id=data1.invoking_login)

            # 获取请求类型
            # 获取token信息

            token = requests.post(url,
                                  json=request_data,
                                  headers=headers)
            if 'token' in token.content:
                headers["Authorization"] = "Jwt " + token.json()['token']
            return headers

    def get_case(self):
        # 查询要运行的套件信息
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            headers = self.login()
            # token = requests.post("http://127.0.0.1:8000/api-auth/",
            #                       json={"username": "zhengxq1",
            #                             "password": "zxq111111"},
            #                       headers={
            #                           "Content-Type":
            #                               "application/json; charset=utf-8"})
            # headers["Authorization"] = "Jwt " + token.json()['token']
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            assert_type = data1.assert_value
            except_result = data1.expected_result
            t = requests.get(url, json=request_data, headers=headers,
                             verify=False)
            # 判断'==、!=、not in、in四种情况下的预期结果和接口返回结果的校验。
            # 校验结果通过更改状态为成功，校验结果未通过更改状态为失败'
            if assert_type == '==':
                if except_result.encode('utf-8') in t.content:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='成功')
                    Case.objects.filter(isdelete=False,
                                        case_name=data.case.case_name).update(
                        result=t.json())

                    return Response(t.json(), status=status.HTTP_200_OK,
                                    headers=headers)
                # return Response(t)
                else:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='失败')
                    return Response(t.json(), status=t.status_code,
                                    headers=headers)
        except Exception as e:
            return Response(e)

    def post_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            print(url, request_data)
            headers = self.login()
            print(headers)
            if request_data == '':
                request_data = {}
            # 请求参数未填写情况下赋值空值
            t = requests.post(url, json=eval(request_data),
                              headers=headers, verify=False)
            print(t.json())
            assert_type = data1.assert_value
            except_result = data1.expected_result
            if assert_type == '==':
                if except_result.encode('utf-8') in t.content:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='成功')
                    Case.objects.filter(isdelete=False,
                                        case_name=data.case.case_name).update(
                        result=t.json())

                    return Response(t.json(), status=status.HTTP_200_OK,
                                    headers=headers)
                else:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='失败')
                    return Response(t.json(), status=t.status_code,
                                    headers=headers)
        except Exception as e:
            return Response(e)

    def put_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            headers = self.login()
            assert_type = data1.assert_value
            except_result = data1.expected_result
            if request_data == '':
                request_data = {}
            t = requests.put(url, json=eval(request_data),
                             headers=headers, verify=False)
            if assert_type == '==':
                if except_result.encode('utf-8') in t.content:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='成功')
                    Case.objects.filter(isdelete=False,
                                        case_name=data.case.case_name).update(
                        result=t.json())

                    return Response(t.json(), status=status.HTTP_200_OK,
                                    headers=headers)
                # return Response(t)
                else:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='失败')
                    return Response(t.json(), status=t.status_code,
                                    headers=headers)
        except Exception as e:
            return Response(e)

    def delete_case(self):
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取请求地址
            url = data.yuming.url_name + data1.url
            # 获取请求数据
            request_data = data1.request_data
            # 获取请求类型
            # 获取token信息
            assert_type = data1.assert_value
            except_result = data1.expected_result
            headers = self.login()
            t = requests.delete(url, json=eval(request_data),
                                headers=headers, verify=False)
            if assert_type == '==':
                if except_result.encode('utf-8') in t.content:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='成功')
                    Case.objects.filter(isdelete=False,
                                        case_name=data.case.case_name).update(
                        result=t.json())

                    return Response(t.json(), status=status.HTTP_200_OK,
                                    headers=headers)
                # return Response(t)
                else:
                    Case_suite.objects.filter(
                        suite_id=serializers['suite_id']).update(
                        status='失败')
                    return Response(t.json(), status=t.status_code,
                                    headers=headers)
        except Exception as e:
            return Response(e)

    def post(self, request):
        return_message = {"code": 200, "message": "success"}
        # 获取前端提交的数据
        global serializers
        serializers = request.data
        # 查询要运行的套件信息
        data = Case_suite.objects.get(suite_id=serializers['suite_id'])
        # 查询测试套件下对应的测试用例信息
        data1 = Case.objects.filter(isdelete=False).get(
            case_name=data.case.case_name)
        try:
            # 获取headers
            # # 获取请求地址
            url = data.yuming.url_name + data1.url
            # # 获取请求数据
            request_data = data1.request_data
            # # 获取请求类型
            request_type = data1.request_type
            # # 获取token信息
            headers = self.login()
            assert_type = data1.assert_value
            except_result = data1.expected_result
            # 请求参数未填写情况下赋值空值
            # if request_data == '':
            #     request_data = {}
            # get请求处理
            logging.debug('不调用其他接口返回数据')
            if data1.case_bz == "":
                if request_type == 'get':
                    results = self.get_case()
                    return Response(results.data)
                # post请求处理
                if request_type == 'post':
                    results = self.post_case()
                    return Response(results.data)
                # put请求处理
                if request_type == 'put':
                    results = self.put_case()
                    return Response(results.data)
                # delete请求处理
                if request_type == 'delete':
                    results = self.delete_case()
                    return Response(results.data)
            if data1.case_bz != "":
                for i in eval(data1.case_bz):
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
                                eval(Case.objects.get(case_id=i).result)[
                                    t2])
                            new_body = ''
                            for i in body_res:
                                new_body = request_data.replace(i, str(
                                    url_pattern))
                            # 查询上一个接口返回的数据，替换url中的参数

                            new_url = url.replace(t1, str(url_pattern))
                            if request_type == 'put':
                                t = requests.put(new_url,
                                                 json=new_body,
                                                 headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                            if request_type == 'post':
                                t = requests.post(new_url,
                                                  json=new_body,
                                                  headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                            if request_type == 'get':
                                t = requests.get(new_url,
                                                 json=new_body,
                                                 headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)

                            if request_type == 'delete':
                                t = requests.delete(new_url,
                                                    json=new_body,
                                                    headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                        elif t1 and len(body_res) == 0:
                            t1 = t1.group(0)
                            t2 = t1.replace('[', '')
                            t2 = t2.replace(']', '')
                            url_pattern = (
                                eval(Case.objects.get(case_id=i).result)[
                                    t2])
                            # 查询上一个接口返回的数据，替换url中的参数

                            new_url = url.replace(t1, str(url_pattern))
                            if request_type == 'put':
                                t = requests.put(new_url,
                                                 json=eval(request_data),
                                                 headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:

                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                                return Response(return_message)
                            if request_type == 'post':
                                t = requests.post(new_url,
                                                  json=eval(request_data),
                                                  headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                                return Response(return_message)
                            if request_type == 'get':
                                t = requests.get(new_url,
                                                 json=request_data,
                                                 headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                                return Response(return_message)

                            if request_type == 'delete':
                                t = requests.delete(new_url,
                                                    json=request_data,
                                                    headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=
                                                            data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                                return Response(return_message)
                        if not t1 and len(body_res) > 0:
                            # 将【】替换为空
                            new_data = request_data
                            for body in body_res:
                                new_body = body.replace('[', '')
                                new_body = str(new_body).replace(']', '')
                                new_body = eval(
                                    Case.objects.get(case_id=i).result)[
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
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                            if request_type == 'post':
                                t = requests.post(url,
                                                  json=eval(new_data),
                                                  headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                            if request_type == 'get':
                                t = requests.get(url,
                                                 json=new_data,
                                                 headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=
                                                        status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)

                            if request_type == 'delete':
                                t = requests.delete(url,
                                                    json=new_data,
                                                    headers=headers)
                                if assert_type == '==':
                                    if except_result.encode(
                                            'utf-8') in t.content:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='成功')
                                        Case.objects.filter(isdelete=False,
                                                            case_name=data.case.case_name
                                                            ).update(
                                            result=t.json())

                                        return Response(t.json(),
                                                        status=status.HTTP_200_OK,
                                                        headers=headers)
                                    else:
                                        Case_suite.objects.filter(
                                            suite_id=serializers[
                                                'suite_id']).update(
                                            status='失败')
                                        return Response(t.json(),
                                                        status=t.status_code,
                                                        headers=headers)
                        return Response(return_message)
                    except Exception as e:
                        return Response(e)

        except Exception as e:
            return Response(e)
