#!/usr/bin/env python
# coding=utf-8
import pymysql.cursors

class Users_id(object):
    def __init__(self,user_id):
        self.user_id = user_id

    def get_ideas(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql="select shuoshuo,time from shuoshuo_me where user_id=%s order by time desc"
                cursor.execute(sql,(self.user_id))
                result=cursor.fetchall()
            print('hahahaahah')
        finally:
            connection.close()

        return result
    def get_friends(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql = "select friends_name from friends where the_user_id=%s"
                cursor.execute(sql,(self.user_id))
                result=cursor.fetchall()
                print(result)

        finally:
            connection.close()
        return result
