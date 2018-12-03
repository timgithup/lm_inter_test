#-*- coding:utf-8 -*-
'''
Created on 2018-11-12

@author: Administrator
'''
import json
import os

class OperationJson:
    def __init__(self, file_path=None):
        if file_path == None:
            self.file_path = '../data/testjson.json'
        else:
            self.file_path = file_path
            
        if os.path.getsize(self.file_path) == 0:
            self.write_data('DATA')   
        self.data = self.read_data()
    
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data
        
    def get_data(self, key):
        return self.data[key]
    
    def write_data(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))
    
if __name__ == "__main__":
    opers = OperationJson('../data/cookies.json')
    print opers.get_data('test')