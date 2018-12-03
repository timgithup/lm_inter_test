#coding:utf-8
'''
Created on 2018-11-15

@author: Administrator
'''
class CommonUtil:
    def is_contain(self, str_one, str_two):
        flag = None
#         if isinstance(str_one, unicode):
#             str_one = str_one.encode('unicode-escape').decode('string_escape')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag