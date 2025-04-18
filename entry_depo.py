import mysql.connector
from tkinter import messagebox


def entry_det(acno1,ddate,amt,rem):
    
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
    mycon.autocommit=True
    cursor=mycon.cursor()

    s='use niraj'
    cursor.execute(s)

    remark = 'NP'
    
    cursor.execute("select remark from cusinfo where acno = {}".format(acno1))
    r=0
    for i in cursor:
        r=i[0]
    
    if (r=='A'):
        s="insert into deposit values({},'{}',{},'{}','{}')".format(acno1,ddate,amt,rem,remark)
        cursor.execute(s)
    else:
        messagebox.showinfo("ERROR!","Your Ac Has Been Closed")
    

    cursor.execute("select closingbal from closibal where acno = {}".format(acno1))
    closingbal=0
    for i in cursor:
        closingbal=i[0]

    cursor.execute("update closibal set Closingbal={}, ldate='{}' where acno={}".format((closingbal+amt),ddate,acno1))





