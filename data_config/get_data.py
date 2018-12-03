#coding:utf-8
'''
Created on 2018-11-12

@author: Administrator
'''
from unit.oper_excel  import OperationExcel
from unit.oper_json import OperationJson
from unit.oper_txt import OperationTxt
from unit.oper_oracleldb import OperationOracle
import dataconfig


class GetData:
    def __init__(self):
        self.operEx = OperationExcel()
        
    def get_case_lines(self):
        case_lines = self.operEx.get_lines()
        return case_lines
    
    def get_request_url(self,row):
        col = dataconfig.get_url()
        url = self.operEx.get_cell_value(row, col)
        return url       
     
    def get_method(self, row):
        col = dataconfig.get_request_way()
        method = self.operEx.get_cell_value(row, col)
        return method
    
    def get_is_run(self, row):
        flag = None
        col = dataconfig.get_run()
        run_model = self.operEx.get_cell_value(row, col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag
    
    def get_is_header(self, row):
        col = dataconfig.get_header()
        header = self.operEx.get_cell_value(row, col)
        return header

    
    def get_request_data(self, row):
        col = dataconfig.get_data()
        request_data = self.operEx.get_cell_value(row, col)
        if request_data == '':
            return None
        else:
            return request_data
    
    def get_request_data_for_json(self, row):
        operJson = OperationJson()
        json_request_data = operJson.get_data(self.get_request_data(row))
        return json_request_data
    
    def get_expect(self, row):
        col = dataconfig.get_expect()
        expect = self.operEx.get_cell_value(row, col)
        return expect
    
    def get_expect_from_db(self, row):
        oper_db = OperationOracle()
        sql = self.get_expect(row)
        expect = oper_db.serch_one(sql)
        return expect.decode('unicode-escape')
    
    def write_resule(self, row, value):
        col = dataconfig.get_relust()
        self.operEx.write_value(row, col, value)
    
    def get_depend_case(self, row):
        col = dataconfig.get_case_depend()
        depend_case = self.operEx.get_cell_value(row, col)
        if depend_case == None:
            return None
        else:
            return depend_case        
    
    #获取依赖数据的key    
    def get_depend_data(self, row):
        col = dataconfig.get_data_depend()
        depend_data = self.operEx.get_cell_value(row, col)
        if depend_data == None:
            return None
        else:
            return depend_data
        
    def get_depend_field(self, row):
        col = dataconfig.get_field_depend()
        depend_field = self.operEx.get_cell_value(row, col)
        if depend_field == None:
            return None
        else:
            return depend_field
        
    def get_email_user_list(self):
        user_list = OperationTxt().get_email_user_list()
        return user_list
                
        
    
if __name__ == "__main__":
    aa = GetData()
    print aa.get_is_run(2)