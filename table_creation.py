import mysql.connector


mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)

#created customer detail table
s='create table if not exists cusinfo(acno integer,name varchar(25),father varchar(25),add1 varchar(25),add2 varchar(25),lm varchar(25),city varchar(25),pin integer,mobileno integer,dob date,email varchar(25),gender varchar(25),remark varchar(5),password varchar(12),pan varchar(15),adh varchar(15))'
cursor.execute(s)

#created deposit table
s="create table if not exists deposit(acno integer,ddate date,amt integer,rem varchar(5),Remark varchar(5))"
cursor.execute(s)

#created withdrew table
s='create table if not exists withdrew(acno integer,wdate date,amt decimal,Remark varchar(5))'
cursor.execute(s)

#created balance table
s="create table if not exists closibal(acno integer,ldate date,ClosingBal integer)"
cursor.execute(s)
