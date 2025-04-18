
from tkinter import *
from PIL import Image,ImageTk
import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)

def witdw(acno2):
    
    s="update closibal set ClosingBal={} where acno={}".format(0,acno2)
    cursor.execute(s)

def wthdr(acno2,date1,wamt):

    s="insert into withdrew values({},'{}',{})".format(acno2,date1,wamt)
    cursor.execute(s)
    
def dadte1(d1):
    cursor.execute("select *from deposit where ddate='{}'".format(d1))
    for row in cursor:
        print (row)
    cursor.execute("select *from withdrew where wdate='{}'".format(d1))
    for row in cursor:
        print (row)

def dadte(d1,d2):
    cursor.execute("select *from deposit where ddate between ddate='{}' and ddate='{}'".format(d1,d2))
    for row in cursor:
        print (row)
    cursor.execute("select *from withdrew where wdate between wdate='{}' and wdate='{}'".format(d1,d2))
    for row in cursor:
        print (row)
                   
