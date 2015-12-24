#!/usr/bin/env python3
# _*_ coding:utf-b _*_

'mysql'

__author__=zhangjian

 
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='a1836810995',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
         sql = "insert into kongjian (id,shuoshuo) values(%s,%s)"
         cursor.execute(sql, ('happy pinganye'))
 
    connection.commit()

    with connection.cursor() as cursor:
         sql = "select 'id','shuoshuo' from kongjian"
         result=fetchone()
         print(result)
finally:
	connection.close()
