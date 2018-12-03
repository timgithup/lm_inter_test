#coding:utf-8
'''
Created on 2018-11-18

@author: Administrator
'''
from unit.oper_excel import OperationExcel
from base.run_method import RunMethod
from data_config.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json

class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.operEx = OperationExcel()
        self.data = GetData()
    
    def get_case_line_data(self):
        rows_data = self.operEx.get_row_datas(self.case_id)
        return rows_data
    
    def run_depend(self):
        run_method = RunMethod()
        row_num = self.operEx.get_row_num(self.case_id)

        url = self.data.get_request_url(row_num)
        method = self.data.get_method(row_num)
        request_data = self.data.get_request_data_for_json(row_num)
        header = self.data.get_is_header(row_num)
        if header == 'yes':
            res = run_method.run_main(url, method, request_data, header)
        else:
            res = run_method.run_main(url, method, request_data)
        return json.loads(res)
    
    def get_data_for_key(self, row):
        depend_data =  self.data.get_depend_data(row)
        response_data = self.run_depend()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
        