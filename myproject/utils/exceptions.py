from rest_framework.views import exception_handler

#
# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         print(response.data)
#         response.data.clear()
#         response.data['code'] = response.status_code
#         response.data['data'] = []
#
#         if response.status_code == 404:
#             try:
#                 response.data['message'] = response.data.pop('detail')
#                 response.data['message'] = "Not found"
#             except KeyError:
#                 response.data['message'] = "Not found"
#
#         if response.status_code == 400:
#             response.data['message'] = '参数错误'
#
#         elif response.status_code == 401:
#             response.data['message'] = "认证失败"
#
#         elif response.status_code >= 500:
#             response.data['message'] = "服务器异常"
#
#         elif response.status_code == 403:
#             response.data['message'] = "Access denied"
#
#         elif response.status_code == 405:
#             response.data['message'] = 'Request method error'
#     return response


from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        error_msg_list = []
        for key, value in response.data.items():
            if isinstance(value, list):
                error_msg_list.append('%s参数有误：%s' % (key, ' '.join(value)))
            else:
                error_msg_list.append(str(value))
            del response.data[key]
        response.data['message'] = '\n'.join(error_msg_list)
        response.data['status_code'] = response.status_code
    return response
