#!/usr/bin/env python
# -*- coding:utf-8 -*-


import cx_Oracle
from unit.oper_txt import OperationTxt


class OperationOracle:
    #在Oracle中查询数据
    def __init__(self):
        '''
            connect_info='emssxjk/emssxjk@orcl'
        '''
        connect_info = OperationTxt().get_db_conn_info()
        self.conn = cx_Oracle.connect(connect_info)
        self.cur = self.conn.cursor()

    #获取一条记录
    def serch_one(self, sql):
        self.cur.execute(sql)     
        one = self.cur.fetchone()
        return one
        print '1: id:%s,name:%s,password:%s'%one
        self.cur.close()
        self.conn.close()
        
    #获取两条记录!!!注意游标已经到了第二条    
    def serch_tow(self, sql):
        self.cur.execute(sql)     
        two = self.cur.fetchmany(2)
        return two
        print '2 and 3:',two[0],two[1]
        self.cur.close()
        self.conn.close()

    #全部数据
    def serch_all(self, sql):
        self.cur.execute(sql)    
        all_res = self.cur.fetchall();
        for row in all_res:
            print row   #打印所有结果
        return all_res
        self.cur.close()
        self.conn.close()

    #条件查询
    def serch_by_par(self, sql, par):
        '''sql="""select * from tb_user where id <= :id"""
           par=5
        '''
        self.cur.prepare(sql)
        self.cur.execute(None,{'id':par})
        for row in self.cur:  #相当于fetchall()
            print row
        self.cur.close()
        self.conn.close()

