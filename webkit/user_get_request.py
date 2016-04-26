#!/usr/bin/env python
# coding=utf-8
import pymysql.cursors

class Users(object):
    def __init__(self,the_user_id,account_number = 1):
        self.account_number = account_number
        self.the_user_id = the_user_id

    def get_request(self):
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql = "select friends_name from request where the_account_number=%s"
                cursor.execute(sql,(self.account_number))
                result=cursor.fetchall()

        finally:
            connection.close()
        return result

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
                cursor.execute(sql,(self.the_user_id))
                result=cursor.fetchall()

        finally:
            connection.close()
    
        return result
