#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2019/12/30 14:44:09
@Author  :   刘华强
@Contact :   1761512493@qq.com
'''
import pymysql
#创建连接
db = pymysql.connect(db='test', user='root', password='123456', host='127.0.0.1', port=3306,charset='utf8')
#创建浮标
cursor = db.cursor()
# sql = "DELETE FROM `test`.`score` WHERE  `name`='杨川' AND `score`=100 LIMIT 1;"
try :
    sql = "select * from score"
    cursor.execute(sql)
    txt  = cursor.fetchall()
    if len(txt)!=0:
        print(len(txt))
        for info in txt :
            print(info)
except:
    print("操作失败")
cursor.close()
db.commit()
db.close()