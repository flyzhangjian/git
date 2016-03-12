#!/usr/bin/env python
# coding=utf-8
from flask import Flask,request,render_template,session
import pymysql.cursors
app=Flask(__name__)

@app.route('/')
def init():
    return render_template('zhuye.html')

@app.route('/user',methods=['post','get'])
def user():
    connection=pymysql.cursors(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql="show tables"
            cursor.execute(sql)
            result=cursor.fetchall()
        connection.commit()
    finally:
        connection.close()
    return render_template('user.html',database=result)


if __name__ == '__main__':
    app.run(debug='True')
