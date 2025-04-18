import mysql.connector

mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)

def updated(dt,ac):
    cursor.execute("update deposit set Remark='{}' where ddate='{}' and acno={}".format('P',dt,ac))

def updatew(dt,ac):
    cursor.execute("update withdrew set Remark='{}' where wdate='{}' and acno=".format('P',dt,ac))  
