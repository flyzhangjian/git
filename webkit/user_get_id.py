#!/usr/bin/env python
# coding=utf-8

import pymysql.cursors

class Users(object):
    def __init__(self,account_number_me,friends_name = 'zhang'):
        self.account_number_me = account_number_me
        self.friends_name = friends_name

    def get_user_id(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'        
            )
        try:
            with connection.cursor() as cursor:
                sql="select user_id from user_me where account_number=%s"
                cursor.execute(sql,(self.account_number_me))
                result=cursor.fetchall()
                print(result)
                user_id=result[0][0]
                print(user_id)
        finally:
            connection.close()

        return user_id
    def get_friends_id(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql = "select user_id from user_me where user=%s"
                cursor.execute(sql,(self.friends_name))
                result=cursor.fetchall()

        finally:
            connection.close()

        return result
