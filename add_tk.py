import mysql.connector
from tkinter import messagebox
import tkinter as tk
import datetime
import update_tk as upt

mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)
def add_dep_with(ac):
    

    m=[]
    l=[]
    
    cursor.execute("select remark from cusinfo where acno = {}".format(ac))
    for i in cursor:
        if(i[0] == 'A'):
            cursor.execute("select Remark from deposit where acno = {}".format(ac))
            for i in cursor:    
                if(i[0]=='NP' or i[0]=='None'):
                    cursor.execute("select ddate,amt from deposit where acno = {}".format(ac))
                    for i in cursor:
                        dt = i[0]
                        
                        m.append(dt.strftime("%Y-%m-%d"))
                        m.append(i[1])
                        m.append("D")
                        l.append(m)
                        upt.updated(dt,ac)
                        m=[]
                else:
                    
                    messagebox.showinfo("ERROR!","You PassBook is Updated")
            
                        

            cursor.execute("select Remark from withdrew where acno = {}".format(ac))
            for i in cursor:    
                if(i[0]=='NP' or i[0]=='None'):
                    cursor.execute("select wdate,amt from withdrew where acno = {}".format(ac))
                    for i in cursor:
                        dt = i[0]
                        
                        m.append(dt.strftime("%Y-%m-%d"))
                        m.append(float(i[1]))
                        m.append("W")
                        l.append(m)
                        upt.updatew(dt,ac)
                        m=[]
                    
                        

            l.sort()
            return(l)
        else:
            messagebox.showinfo("ERROR!","You A/C is Not Active")
            


def add_cb(ac):
    cursor.execute("select remark from cusinfo where acno = {}".format(ac))
    for i in cursor:
        if(i[0] == 'A'):
            cursor.execute("select ClosingBal from closibal where acno = {}".format(ac))
            for i in cursor:
                return(i[0])

def display_pb(l,cb):
    root = tk.Tk()
    root.title("PASSBOOK PRINT")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" WITHDREW&DEPOSIT ",fg="blue")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=10,width=60)
    text_box1.grid(row=0,column=1)

    for data in range(len(l)) :
        text_box1.insert(tk.END,l[data][0]+',')
        text_box1.insert(tk.END,l[data][1])
        text_box1.insert(tk.END,','+l[data][2])
        text_box1.insert(tk.END,"\n")


    name_label = tk.Label(main_frame,text=" CLOSINGBAL ",fg="blue")
    name_label.grid(row=1,column=0)
    
    text_box2 = tk.Text(main_frame,height=2,width=30)
    text_box2.grid(row=1,column=1)

    text_box2.insert(tk.END,cb )
    
        
#add_dep_with(105634)
