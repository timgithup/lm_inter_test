'''
Created on 2018-11-10

@author: Administrator
'''
import requests
import json

class RunMethod:
    #def __init__(self,url, method, data=None):
    #    self.res = self.run_main(url, method, data)
    
    def post_main(self,url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        print res.status_code
        return res.json()
    
    def get_main(self,url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, params=data, verify=False)
        print res.status_code
        return res.json()
    
    def run_main(self,url, method, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)

        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)

# if __name__ == '__main__':
#     url = 'http://127.0.0.1:8000/login/'
#     data = {
#             'username':'lmtest',
#             'password':'123'
#             }
#     run = RUN_MAIN(url, 'POST', data)
#     print run.res