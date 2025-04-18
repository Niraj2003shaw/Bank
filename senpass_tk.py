import mysql.connector

def passes_tk(acno1):
    
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
    mycon.autocommit=True
    cursor=mycon.cursor()

    s='use niraj'
    cursor.execute(s)
    cursor.execute("select password from cusinfo where acno={} and remark='{}'".format(acno1,'A'))
    for i in cursor:
        return(i[0])
    




