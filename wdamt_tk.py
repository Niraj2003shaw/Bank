import tkinter as tk
import mysql.connector
import senbaln_tk as sbt
from tkinter import messagebox
import tkinter as tk


def withamt(acno,wdate):

    def checkvalid():
        checkvalid_tk(acno,wdate)

    def checkvalid_tk(acno,wdate):
        input_amt = text_box1.get("1.0",tk.END)

        mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
        mycon.autocommit=True
        cursor=mycon.cursor()

        s='use niraj'
        cursor.execute(s)
        
        p=sbt.bal_tk(acno)
        amt = int(input_amt.strip())
        root.destroy()

        if (p>amt):
            
            cursor.execute("select remark from cusinfo where acno = {}".format(acno1))
            r=0
            for i in cursor:
                r=i[0]
            if (r=='C'):

                messagebox.showinfo("ERROR!","Your Ac Has Been Closed")

            else:
                p = p-amt
                if(p<=1000):
                    p = p-(p*.02)
                    messagebox.showinfo("OKAY!","But Minimum Balance Hitting")
                messagebox.showinfo("OKAY!","Your Amount Withdrew")
                remark = 'NP'
            
                s="insert into withdrew values({},'{}',{},'{}')".format(acno,wdate,amt,remark)
                cursor.execute(s)
        else:
            messagebox.showinfo("ERROR!","You Are Out Of Balance")

        cursor.execute("update closibal set ClosingBal={}, ldate='{}' where acno={}".format(p,wdate,acno))   
            

    root = tk.Tk()
    root.title("WITHDRAWAL AMOUNT")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" AMOUNT ",fg="black")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=checkvalid)
    store_button.grid(row=13,column=1)

    root.mainloop()



