import mysql.connector
from datetime import date


def entry_det(acno,name,father,add1,add2,lm,city,pin,mobileno,dob,email,gender,password,pan,adh):
    
    mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
    mycon.autocommit=True
    cursor=mycon.cursor()

    s='use niraj'
    cursor.execute(s)

    
    cursor.execute(s)

    remark = "A";

    

    s="insert into cusinfo values({},'{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}','{}')".format\
                                (acno,name,father,add1,add2,lm,city,int(pin),int(mobileno),dob,email,gender,remark,password,pan,adh)
    cursor.execute(s)

    print(password)

    ddate=date.today()
    amt=0

    s="insert into closibal values({},'{}',{})".format(acno,ddate,amt)
    cursor.execute(s)

