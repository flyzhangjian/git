#!/usr/bin/env python
# coding=utf-8
import pymysql.cursors

def connection_out():
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        db = 'kongjian',
        password = '123456',
        charset = 'utf8',
        cursorclass = pymysql.cursors.DictCursor
        )
    return connection
