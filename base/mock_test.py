#coding:utf-8
'''
Created on 2018-11-12

@author: Administrator
'''
from mock import mock

def MockTest(method_name, url, method, data):
    method_name = mock.Mock(return_value=data)
    res = method_name(url, method, data)
    return res