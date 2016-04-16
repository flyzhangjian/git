#!/usr/bin/env python
# coding=utf-8

import pymysql.cursors

class Users(object):
    def __init__(self,account_number_me,user_id,friends_name):
        self.account_number = account_number_me
        self.user_id = user_id
        self.friends_name = friends_name

    def get_user_account_number(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql = "select account_number from user_me where user_id=%s"
                cursor.execute(sql,(self.user_id))
                result=cursor.fetchall()

        finally:
            connection.close()
    
        return result
