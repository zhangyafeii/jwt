# -*- coding: utf-8 -*-

"""
@Datetime: 2019/1/16
@Author: Zhang Yafei
"""
# from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware


class MiddlewareMixin:
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):
    """
    cors跨域实现简答请求
    跨域：向不同域名或端口不同的地址发送请求）
    """

    def process_response(self, request, response):
        # 添加响应头
        #
        # 允许你的域名来获取我的数据
        # response['Access-Control-Allow-Origin'] = "*"
        #
        # 允许你携带Content-Type请求头
        # response['Access-Control-Allow-Headers'] = "Content-Type"
        #
        # 允许你发送DELETE,PUT
        # response['Access-Control-Allow-Methods'] = "DELETE,PUT"
        response['Access-Control-Allow-Origin'] = "*"

        if request.method == 'OPTIONS':
            response['Access-Control-Allow-Headers'] = "Content-Type"
            response['Access-Control-Allow-Methods'] = "DELETE,PUT"

        return response