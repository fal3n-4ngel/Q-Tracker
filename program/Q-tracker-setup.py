import mysql.connector as sqltor

user=input('Enter Mysql username:')
passw=input('enter Mysql password:')
mycon=sqltor.connect(host='localhost',user=user,password=passw)
cursor=mycon.cursor(buffered=True)

cmd1='create database qtracker'
cmd2='use qtracker'
cmd3='create table corona(id varchar(10),name varchar(25),loc varchar(10),address varchar(30),phone varchar(10),date date,time time,result varchar(10))'
cmd3='create table id(count int)'
cmd4='insert into id values(0)'
licmd=[cmd1,cmd2,cmd3,cmd4]
for i in licmd:
	cursor.execute(i)
	mycon.commit()

print('DONE.....')
input()
