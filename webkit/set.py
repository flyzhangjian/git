#!/usr/bin/env python
# coding=utf-8

import json
from flask import Flask,request,render_template,session
import time
import user_get_id,user_get_ideas,user_get_request 
import connect
from flask.ext.bootstrap import Bootstrap

app=Flask(__name__)
bootsteap = Bootstrap(app)

def get_time():
    return time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))


@app.route('/')
def init():
    return render_template('zhuye.html')

@app.route('/set.html',methods=['GET'])
def zhuye():
    return render_template('set.html')

@app.route('/zhuye.html',methods=['POST'])
def set():
    time=get_time()
    connection = connect.connection_out()
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
    get_id = user_get_id.Users(account_number_me)
    user_id = get_id.get_user_id()
    connection = connect.connection_out()
    try:
        with connection.cursor() as cursor:
            sql="select password,user from user_me where account_number = %s"
            cursor.execute(sql,account_number_me)
            result=cursor.fetchall()
        print(result)
        password=int(result[0]['password'])
        if password_me==password:
            session['the_user_id']=user_id
            session['name']=result[0]['user']
            check=json.dumps({"result":1})
            return check
        else:
            check=json.dumps({"result":0})
            return check

    finally:
        connection.close()

@app.route('/log_in.html',methods=['POST','GET'])
def log_in_done():
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    the_idea = gets_ideas.get_ideas()
    return render_template('log_in.html',name = session['name'],shuoshuo = the_idea)

@app.route('/check_account_number',methods=['POST'])
def check_account_number():
    account_number_me = int(request.form['account_number'])
    connection = connect.connection_out()
    try:
        with connection.cursor() as cursor:
            sql = "select account_number from user_me"
            cursor.execute(sql)
            result = cursor.fetchall()
            for i in result:
                if account_number_me == i['account_number']:
                    return json.dumps({"result":1})
            return json.dumps({"result":0})
    finally:
        connection.close()
            

@app.route('/my_friends',methods=['POST','GET'])
def get_my_friends():
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    my_friends=json.dumps(gets_ideas.get_friends())
    print(my_friends)
    return my_friends

@app.route('/my_thoughts',methods=['POST'])
def my_thoughts():
    time=get_time()
    connection = connect.connection_out()
    try:
        with connection.cursor() as cursor:
            sql="insert into shuoshuo_me (user_id,shuoshuo,time) values (%s,%s,%s)"
            cursor.execute(sql,(session['the_user_id'],request.form['my_thoughts'],time))
        connection.commit()

    finally:
        connection.close()
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    the_idea=gets_ideas.get_ideas()
    my_friends=gets_ideas.get_friends()
    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)

@app.route('/friend',methods=['post'])
def search_friend():
    account_number=int(request.form['account_number'])
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    the_idea=gets_ideas.get_ideas()
    my_friends=gets_ideas.get_friends()
    connection = connect.connection_out()
    try:
        with connection.cursor() as cursor:
            sql = "insert into request (friends_name,the_account_number) values (%s,%s)"
            cursor.execute(sql,(session['name'],account_number))

        connection.commit()

    finally:
        connection.close()

    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)


@app.route('/log_out',methods=['post','get'])
def log_out():
    session.pop('name',None)
    session.pop('the_user_id',None)
    print(session)
    return render_template('zhuye.html')

@app.route('/the_request',methods=['POST','get'])
def the_request():
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    my_friends=gets_ideas.get_friends()
    gets_user_account_number=user_get_request.Users(session['the_user_id'])
    account_number_me = gets_user_account_number.get_user_account_number()
    gets_user_account_number = user_get_request.Users(session['the_user_id'],account_number_me[0][0])
    requests=gets_user_account_number.get_request()

    return render_template('log_in_friends.html',name=session['name'],friends=my_friends,request=requests)

@app.route('/my_thoughts_me',methods=['POST','get'])
def my_thoughts_me():
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    my_friends=gets_ideas.get_friends()
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    the_idea=gets_ideas.get_ideas()

    return render_template('log_in.html',name=session['name'],shuoshuo=the_idea,friends=my_friends)

@app.route('/make_friends',methods=['POST'])
def make_friends():
    gets_user_account_number=user_get_request.Users(session['the_user_id'])
    account_number_me = gets_user_account_number.get_user_account_number()
    gets_user_account_number = user_get_request.Users(session['the_user_id'],account_number_me[0][0])
    requests=gets_user_account_number.get_request()
    requests_me=requests[0]
    if request.form['agree']:
        get_id = user_get_id.Users(account_number_me,session['name'])
        the_friends=get_id.get_friends_id()
        the_friends_id=the_friends[0][0]
        connection = connect.connection_out()
        try:
            with connection.cursor() as cursor:
                sql = "delete from request where the_account_number=%s"
                cursor.execute(sql,(account_number_me))
                sql = "insert into friends (the_user_id,his_friends_id,friends_name) values(%s,%s,%s)"
                cursor.execute(sql,(session['the_user_id'],the_friends_id,requests_me))

            connection.commit()
        finally:
            connection.close()
    gets_ideas = user_get_ideas.Users_id(session['the_user_id'])
    my_friends=gets_ideas.get_friends()
    gets_request = user_get_request.Users(session['the_user_id'],account_number_me)
    requests=gets_request.get_request(account_number_me)
    return render_template('log_in_friends.html',name=session['name'],friends=my_friends,request=requests)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'),500
if __name__ == '__main__':
    app.secret_key='DKMKKLFAMKKFMAKLKFJLKHF'
    app.run(debug=True)
