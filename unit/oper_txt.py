#coding:utf-8
'''
Created on 2018-11-19

@author: Administrator
'''

class OperationTxt:
    def get_email_user_list(self):
        data_list = []
        with open('../data/email_user_list.txt') as fp:
            for line in fp:
                data_list.append(line.replace('\n', ''))
        
        return data_list
    
    def get_db_conn_info(self):
        with open('../data/database_connect_info.txt') as fp:
            conn_info = fp.read()
            
        return conn_info
    
if __name__=="__main__":
    run = OperationTxt()
    print run.get_db_conn_info()
            