#!usr/bin/env python3
# _*_ coding:utf-8 _*_

'a test user'

__auther__='zhangjian'

import time,pymysql.cursors

def get_time():
	return strftime('%Y-%m-%d',time.localtime(time.time()))

def check():
	print('please select seting account or logining in by input S or L:')
	a=input()
	if a==S:
		users=set_ha()
	elif a==L:
		users=input_ha()
	return users

def set_ha():
	print('please input your name:')
	user=input()
	print('please set your account number:')
	account_number=int(input())
	print('please set your password:')
	password=int(input())

	time=get_time()
	
	connection=pymysql.connect(host='lacalhost',
							   user='root',
							   password='123456',
							   db='kongjian',
							   charset='utf-8',
							   cursorclass=pymysql.cursors.DictCursor)
	try:
		with connection.cursor() as sursor:
			sql_user="insert into user_me (user,account_number,password,time) values(%s,%s,%s,%s)"
			cursor.execute(sql_user,(user,account_number,password,time))
		connection.commit()
	finally:
		connection.close()
	return user

def input_ha():
	print('please input your user name:')
	user_ha=input()
	print('please input your account number:')
	account_number_ha=int(input())
	print('please input your password:')
	password_ha=int(input())
	
	connection=pymysql.connect(host='lacalhost',
                               user='root',
                               password='123456',
                               db='kongjian',
                               charset='utf-8',
                               cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql="select (account_number,password,user_id) from user_me where user=%s"
			cursor.execute(sql,(user_ha))
			result=cursor.fetchall()
	finally:
		connection.close()
	if account_number_ha==result['account_number'] and password_ha==result['password'] :

		enter(user_ha)
	else :			
		print('the password is wrong')			
	return user_ha

def the_idea(user):
	user_ha=user
	print('please write your ideas:')
	idea=input()
	time=get_time()
	user_id_ha=get_user_id(user_ha)
	connection=pymysql.connect(host='localhost',
							   user='root',
							   password='123456',
						       db='kongjian',
							   charset='utf8',
							   cursorclass=pymysql.cursors.DictCursor)

	try:
		with connection.cursor() as cursor:
			sql="insert into kongjian_me(shuoshuo,time,user_id) values(%s,%s,%s)"
			cursor.execute(sql,(idea,time,user_id_ha))
		connection.commit()

	finally:
		cnnection.close()
	

def enter(user)
	user_ha=user
	user_id_ha=get_user_id(user_ha)
	connection=pymysql.connection(host='localhost',
								  user='root',
								  password='123456',
								  db='kongjian',
								  charset='utf8')
	try:
		with connection.cursor as cursor:
			sql = "select shuoshuo from shuoshuo_me where user_id=user_id_ha"
			cursor.execute(sql)
			result=cursor.fetchall()
			print(result)
	finally:
		connection.close()

def get_user_id(user_ha)
	connection=pymysql.connection(host='localhost',
								  user='root',
								  password='123456',
								  db='kongjian',
								  charset='utf8')
	try:
		with connection.cursor() as cursor:
			sql = "select user_id from user_me where user=user_ha"
			cursor.execute(sql)
			result=cursor.fetchall()
	finally:
		connection.close()
	return result

def main()
	users_ha=check()
	print('please determain what would you like to do (Y:GO ON N: EXIT:)')
	check_out=input()
	while check_out=Y:
		print('do you want to publish your idea?(Y:yes or N:no)')
		idea_check=input()
		if idea_check=Y:
			the_idea(users_ha)
		else:
			break

		print('do you want to check your ideas? please input Y or N')
		check_out=input()
			if check_out=Y
				enter(users_ha)	
			else:
				break

main()
