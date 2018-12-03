#coding:utf-8
'''
Created on 2018-11-12

@author: Administrator
'''

class GlobalVar:
    Id = 0
    Name = 1
    Url = 2
    Is_run = 3
    Request_way = 4
    Header = 5
    Case_depend = 6
    Data_depend = 7
    Field_depend = 8
    Data = 9
    Expect = 10
    Result = 11
    
def get_case_id():
    return GlobalVar.Id
    
def get_case_name():
    return GlobalVar.Name
    
def get_url():
    return GlobalVar.Url
    
def get_run():
    return GlobalVar.Is_run
    
def get_request_way():
    return GlobalVar.Request_way

def get_header():
    return GlobalVar.Header

def get_case_depend():
    return GlobalVar.Case_depend

def get_data_depend():
    return GlobalVar.Data_depend

def get_field_depend():
    return GlobalVar.Field_depend
    
def get_data():
    return GlobalVar.Data

def get_expect():
    return GlobalVar.Expect

def get_relust():
    return GlobalVar.Result

def get_header_value():
    header = {
              "header":"1234"
              
              }
