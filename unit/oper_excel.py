#coding:utf-8
'''
Created on 2018-11-12

@author: Administrator
'''
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../data/testexcel.xls'
            self.sheet_id = 0
        
        self.data = self.get_data()
    
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return tables.nrows
    
    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)
    
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)
    
    def get_row_datas(self, case_id):
        row_num = self.get_row_num(case_id)
        row_data = self.get_row_values(row_num)
        return row_data
    
    def get_row_num(self, case_id):
        num = 0
        col_datas = self.get_col_values()
        for col_data in col_datas:
            if case_id in col_data:
                return num
            num = num+1
    
    def get_row_values(self, row):
        return self.data.row_values(row)
    
    def get_col_values(self,col=None):
        if col != None:
            cols = self.data.col_values(col)
        else:
            cols = self.data.col_values(0)
        
        return cols 
    
if __name__== '__main__':    
    opers = OperationExcel()
    print opers.get_cell_value(1, 2)
#     operExcel.get_data()
#     print tables.nrows
#     print tables.cell_value(2,3)


