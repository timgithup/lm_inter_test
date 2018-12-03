#!/usr/bin/env python
#coding:utf-8
'''
Created on 2018-11-13

@author: Administrator
'''
import sys
sys.path.append("C:/Users/1/workspace/JKtest")
from base.run_method import RunMethod
from data_config.get_data import GetData
from data_config.depend_data import DependData
from unit.common_util import CommonUtil
from unit.send_email import SendEmail
from unit.oper_header import OperationHeader
from unit.oper_json import OperationJson

class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.send_email = SendEmail()
        
    def go_on_run(self):
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            print '----->is_run: ',is_run
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_method(i)
                request_data = self.data.get_request_data_for_json(i)
                header = self.data.get_is_header(i)
                depend_case = self.data.get_depend_case(i)
                expect  = self.data.get_expect(i)
                print '----->depend_case: ',depend_case
                if depend_case != '':
                    dependdata = DependData(depend_case)
                    depend_respone_data = dependdata.get_data_for_key(i)
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_respone_data
                print '----->header: ',header
                if header == 'write':
                    op_header = OperationHeader(url, method, request_data)
                    op_header.write_cookie()
                    
                    res = self.run_method.run_main(url, method, request_data)
                elif header == 'yes':
                    op_json = OperationJson('../data/cookies.json') 
                    t_key = op_json.get_data('key')
                    cookies = {
                              "id":t_key
                              }
                    
                    res = self.run_method.run_main(url, method, request_data, cookies)
                else:
                    res = self.run_method.run_main(url, method, request_data)
                #print u'----The %s case\' result is：----\n%s' %(i, res)
                #print '------------------------'
                if self.com_util.is_contain(expect, res):
                    self.data.write_resule(i, 'Pass')
                    pass_count.append(i)
                else:
                    self.data.write_resule(i, res)
                    fail_count.append(i)
                print '--->over'
                
        self.send_email.send_main(pass_count, fail_count)
        
if __name__=='__main__':
    run = RunTest()
    print run.go_on_run()
                
