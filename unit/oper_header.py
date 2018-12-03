#coding:utf-8
'''
Created on 2018-11-23

@author: Administrator
'''
import requests
from unit.oper_json import OperationJson
import os

class OperationHeader:
    def __init__(self, url, method, data=None, header=None):
        self.url =url
        self.method = method
        self.data = data
        self.header = header
        
        self.cookie = self.get_cookie()
        
    def get_cookie(self):
        if self.method == 'post':
            if self.header != None:
                cookie = requests.post(url=self.url, data=self.data, headers=self.header, verify=False).cookies
            else:
                cookie = requests.post(url=self.url, data=self.data, verify=False).cookies
        elif self.method == 'get':
            if self.header != None:
                cookie = requests.get(url=self.url, data=self.data, headers=self.header, verify=False).cookies
            else:
                cookie = requests.get(url=self.url, data=self.data, verify=False).cookies        

        cookie_dict = requests.utils.dict_from_cookiejar(cookie)
        return cookie_dict
        
    def write_cookie(self):
        op_json = OperationJson('../data/cookies.json')
        op_json.write_data(self.cookie)
        

if __name__=="__main__":
    url = 'http://www.imooc.com/user/ssologin?token=2XHIfPZ8xjux3U9H72TJ4hGANrP0l_hWxxI-Hs1gdRdCcdbFBUtfzNFLmBNqSIjcQtIpNKTfVOyjII1KCSBSgYfcsU6_3SZ_dq92EAfMy4xfK07bFCHPo7VN4of2wTKl23sg2gOlCj82vvWt7GO_KDBA5hVeeFgoT9DdW14vO2M5H2ZRcMpxKApHbo-jQyizrHKTddEk6xfX9sF06ibXCqfErr8BEHA7ZPm7LXN30qemJoPZiPtl85HsMRLR1lmQ7qhWr6bxJR8,-FQr1yGiA9o&callback=jQuery21009612663181032985_1543049702344&_=1543049702346'
    OperationHeader(url, 'get').write_cookie()
    ff = OperationJson('../data/cookies.json')
    coo = ff.get_data('cvde')
    print coo



        
