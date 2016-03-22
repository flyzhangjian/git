#!/usr/bin/env python
# coding=utf-8
from flask import Flask,request,render_template,session
import pymysql.cursors
app=Flask(__name__)

@app.route('/')
def init():
    return render_template('zhuye.html')

@app.route('/user.html',methods=['post','get'])
def user():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql = "select * from user_me"
            cursor.execute(sql)
            result=cursor.fetchall()
        connection.commit()

    finally:
        connection.close()
    return render_template('user.html',friends=result)
@app.route('/back',methods=['get','post'])
def back():
    return render_template('zhuye.html')

@app.route('/delete.html',methods=['post','get'])
def we():
    return render_template('delete.html')


@app.route('/delete',methods=['post','get'])
def delete():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql = "delete from user_me where user_id=%s"
            cursor.execute(sql,(request.form['the user_id']))
        connection.commit()
    finally:
        connection.close()

    return render_template('zhuye.html')

@app.route('/add.html',methods=['post','get'])
def add():
    return render_template('add.html')

@app.route('/add',methods=['post','get'])
def add_me():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql="insert into user_me(user,password,account_number,time) values(%s,%s,%s,%s) "
            cursor.execute(sql,(request.form['user_name'],request.form['user_password'],request.form['user_time'],request.form['user_account_number']))
        connection.commit()
    finally:
        connection.close()
    return render_template('zhuye.html')

@app.route('/update.html',methods=['post','get'])
def update():
    return render_template('update.html')

@app.route('/update',methods=['post','get'])
def update_me():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql = "update user_me set user=%s,password=%s,time=%s,account_number=%s where user_id=%s"
            cursor.execute(sql,(request.form['user_name'],request.form['user_password'],request.form['user_time'],request.form['user_account_number'],request.form['the_user_id']))
        connection.commit()
    finally:
        connection.close()
    return render_template('zhuye.html')

@app.route('/add_table.html',methods=['post','get'])
def add_table():
    return render_template('add_table.html')

@app.route('/add_table',methods=['post','get'])
def add_table_us():
    connection=pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='kongjian',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql="CREATE TABLE %s (%s varchar(255), %s varchar(255),%s varchar(255))"
            cursor.execute(sql,(request.form['table_name'],request.form['column_a'],request.form['column_b'],request.form['column_c']))
        connection.commit()
    finally:
        connection.close()
    return render_template('zhuye.html')

if __name__ == '__main__':
    app.run(debug='True')
