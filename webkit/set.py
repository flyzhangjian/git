#!/usr/bin/env python
# coding=utf-8

import json

from flask import Flask,request,render_template,session
import pymysql.cursors,time
import user
app=Flask(__name__)

def get_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

def get_user_id(account_number_me):
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
            cursor.execute(sql,(account_number_me))
            result=cursor.fetchall()
            print(result)
            user_id=result[0][0]
            print(user_id)
    finally:
        connection.close()

    return user_id

def get_ideas(user_id):
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
            cursor.execute(sql,(user_id))
            result=cursor.fetchall()

    finally:
        connection.close()

    return result

def get_friends(user_id):
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
            cursor.execute(sql,(user_id))
            result=cursor.fetchall()
            print(result)

    finally:
        connection.close()
    return result

def get_request(the_user_id):
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
            cursor.execute(sql,(the_user_id))
            result=cursor.fetchall()

    finally:
        connection.close()
    return result

def get_user_account_number(the_user_id):
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
            cursor.execute(sql,(the_user_id))
            result=cursor.fetchall()

    finally:
        connection.close()
    
    return result

def get_friends_id(friends_name):
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
            cursor.execute(sql,(friends_name))
            result=cursor.fetchall()

    finally:
        connection.close()

    return result

@app.route('/')
def init():
    return render_template('zhuye.html')

@app.route('/set.html',methods=['GET'])
def zhuye():
    return render_template('set.html')

@app.route('/zhuye.html',methods=['POST'])
def set():
    time=get_time()
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
            sql="insert into user_me (user,password,account_number,time) values (%s,%s,%s,%s)"
            cursor.execute(sql,(request.form['name'],request.form['password'],request.form['account_number'],time))

        connection.commit()

    finally:
        connection.close()
    return render_template('zhuye.html')

@app.route('/log_in',methods=['POST'])
def log_in():
    account_number_me=int(request.form['account_number'])
    password_me=int(request.form['password'])
    user_id=get_user_id(account_number_me)
    test = user.Users(account_number_me,user_id,'test')
    connection=pymysql.connect(
        host='localhost',
        user='root',
        db='kongjian',
        password='123456',
        charset='utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql="select password,user from user_me where account_number = %s"
            cursor.execute(sql,account_number_me)
            result=cursor.fetchall()
            users=[dict(password=row[0],user=row[1]) for row in result]
        password=int(users[0]['password'])
        if password_me==password:
            session['the_user_id']=user_id
            session['name']=users[0]['user']
            check=json.dumps({"result":1})
            return check
        else:
            check=json.dumps({"result":0})
            return check

    finally:
        connection.close()

@app.route('/log_in.html',methods=['POST','GET'])
def log_in_done():
    the_idea = get_ideas(session['the_user_id'])
    return render_template('log_in.html',name = session['name'],shuoshuo = the_idea)

@app.route('/check_account_number',methods=['POST'])
def check_account_number():
    account_number_me = int(request.form['account_number'])
    print(account_number_me)
    connection = pymysql.connect(
        host = 'localhost',
        user = 'root',
        db = 'kongjian',
        password = '123456',
        charset = 'utf8'
        )
    try:
        with connection.cursor() as cursor:
            sql = "select account_number from user_me"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                print(i)
                if account_number_me in i:
                    print("yes")
                    return json.dumps({"result":1})
            return json.dumps({"result":0})
    finally:
        connection.close()
            

@app.route('/my_friends',methods=['POST','GET'])
def get_my_friends():
    my_friends=json.dumps(get_friends(session['the_user_id']))
    print(my_friends)
    return my_friends

@app.route('/my_thoughts',methods=['POST'])
def my_thoughts():
    time=get_time()
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
            sql="insert into shuoshuo_me (user_id,shuoshuo,time) values (%s,%s,%s)"
            cursor.execute(sql,(session['the_user_id'],request.form['my_thoughts'],time))
        connection.commit()

    finally:
        connection.close()
    the_idea=get_ideas(session['the_user_id'])
    my_friends=get_friends(session['the_user_id'])
    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)

@app.route('/friend',methods=['post'])
def search_friend():
    account_number=int(request.form['account_number'])
    the_idea=get_ideas(session['the_user_id'])
    my_friends=get_friends(session['the_user_id'])
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
            sql = "insert into request (friends_name,the_account_number) values (%s,%s)"
            cursor.execute(sql,(session['name'],account_number))

        connection.commit()

    finally:
        connection.close()

    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)


@app.route('/log_out',methods=['post'])
def log_out():
    session.pop('name',None)
    session.pop('the_user_id',None)
    print(session)
    return render_template('zhuye.html')

@app.route('/the_request',methods=['POST','get'])
def the_request():
    my_friends=get_friends(session['the_user_id'])
    account_number_me=get_user_account_number(session['the_user_id'])
    requests=get_request(account_number_me[0][0])

    return render_template('log_in_friends.html',name=session['name'],friends=my_friends,request=requests)

@app.route('/my_thoughts_me',methods=['POST','get'])
def my_thoughts_me():
    my_friends=get_friends(session['the_user_id'])
    the_idea=get_ideas(session['the_user_id'])

    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)

@app.route('/make_friends',methods=['POST'])
def make_friends():
    account_number_me=get_user_account_number(session['the_user_id'])
    requests=get_request(account_number_me[0][0])
    requests_me=requests[0]
    if request.form['agree']:
        the_friends=get_friends_id(requests[0][0])
        the_friends_id=the_friends[0][0]
        print(the_friends_id)
        connection=pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='kongjian',
            charset='utf8'
            )
        try:
            with connection.cursor() as cursor:
                sql = "delete from request where the_account_number=%s"
                cursor.execute(sql,(account_number_me))
                sql = "insert into friends (the_user_id,his_friends_id,friends_name) values(%s,%s,%s)"
                cursor.execute(sql,(session['the_user_id'],the_friends_id,requests_me))

            connection.commit()
        finally:
            connection.close()

#    if request.form['disagree']:
#       connection=pymysql.connect(
#           host='localhost',
#           user='root',
#           password='123456',
#           db='kongjian',
#           charset='utf8'
#           )
#       try:
#           with connection.cursor() as cursor:
#               sql = "delete from request where the_account_number=%s"
#               cursor.execute(sql,(account_number_me))
#
#           connection.commit()
#
#       finally:
#           connection.close()
    my_friends=get_friends(session['the_user_id'])
    requests=get_request(account_number_me)
    return render_template('log_in_friends.html',name=session['name'],friends=my_friends,request=requests)


if __name__ == '__main__':
    app.secret_key='DKMKKLFAMKKFMAKLKFJLKHF'
    app.run(debug=True)
