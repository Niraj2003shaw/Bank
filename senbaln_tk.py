import mysql.connector

def bal_tk(acno1):
    
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
    mycon.autocommit=True
    cursor=mycon.cursor()

    s='use niraj'
    cursor.execute(s)
    cursor.execute("select closingbal from closibal where acno = '{}'".format(acno1))
    for i in cursor:
        return(i[0])




