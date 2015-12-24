#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

'mysql'

__author__='zhangjian'

 
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='kongjian',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
         sql = "insert into kongjian (shuoshuo) values(%s)"
         cursor.execute(sql, ('哈哈'))
 
    connection.commit()

    with connection.cursor() as cursor:
         sql = "select id,shuoshuo from kongjian"
         cursor.execute(sql)
         result=cursor.fetchall()
         print(result)
finally:
	connection.close()
