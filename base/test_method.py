#coding:utf-8
'''
Created on 2018-11-11

@author: Administrator
'''
import unittest
from base.run_method import RunMethod
import HTMLTestRunner
from mock_test import MockTest
from unit.oper_excel import OperationExcel
from unit.oper_json import OperationJson


class Test(unittest.TestCase):
        
    def setUp(self):
        self.run = RunMethod()
        self.ExcelData = OperationExcel()
        self.JsonData = OperationJson()


    def tearDown(self):
        pass

    def test_01(self):
        url = self.ExcelData.get_cell_value(1, 2)
        print url
        data = self.JsonData.get_data(self.ExcelData.get_cell_value(1, 4))
        print data
        
        res = self.run.run_main(url, 'POST', data)
        print res
#         self.assertEqual(res['usr'], 'test1', '失败')
#         globals()['usr1'] = res['usr']
     
#     @unittest.skip('test_02')
#     def test_02(self):
#         print usr1
#         url = 'http://127.0.0.1:8000/login/'
#         data = {
#             'username':usr1,
#             'password':'123'
#             }
#         res = self.run.run_main(url, 'POST', data)
#         self.assertEqual(res['usr'], 'lmtest', '失败')
#         
#     def test_03(self):
#         url = 'http://127.0.0.1:8000/login/'
#         data = {
#             'username':'lmtest',
#             'password':'123456'
#             }
#                 
#         print MockTest('self.run.run_main', url, 'POST', data)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    