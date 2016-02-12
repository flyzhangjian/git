#!/usr/bin/env python
# coding=utf-8

from flask import Flask,request,render_template
import pymysql.cursors
app=Flask(__name__)

@app.route('/zhuye.html',methods=['POST'])
def zhuye():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        db='kongjian',
        password='123456',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
        )
    try:
        with connection.cursor() as cursor:
            sql="insert into user_me (user,password,account_number) values (%s,%s,%s)"
            cursor.execute(sql,(request.form['name'],request.form['password'],request.form['account_number']))

        connection.commit()

    finally:
        connection.close()
    return render_template('zhuye.html')

if __name__ == '__main__':
   app.run(debug=True)
