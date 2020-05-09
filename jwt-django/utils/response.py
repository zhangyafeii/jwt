# -*- coding: utf-8 -*-

"""
Datetime: 2020/04/15
Author: Zhang Yafei
Description: 
"""


class BaseResponse(object):
    def __init__(self):
        self.status = 200
        self.msg = None
        self.data = None

    @property
    def dict(self):
        return self.__dict__

