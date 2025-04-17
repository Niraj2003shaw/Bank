import tkinter as tk
import mysql.connector
from tkinter import messagebox



mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)

def deactivate():
    def ac_deactivation():
        input_ac = text_box1.get("1.0",tk.END)

        root.destroy()

        cursor.execute("select  remark from cusinfo   where acno={}".format(input_ac.strip()))

        for row in cursor:
            if(row[0] == 'D'):
                messagebox.showinfo("ERROR"," A/C Is Already De-Activated")
            else:
                cursor.execute("update cusinfo set remark='{}' where acno={}".format('D',input_ac.strip()))
                messagebox.showinfo("SUCCESS","You A/C Is Being De-Activated")

        

    root = tk.Tk()
    root.title("Bank Maneger")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" A/C Number ",fg="#FFD700")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)


    store_button = tk.Button(main_frame,text="SUBMIT",command=ac_deactivation)
    store_button.grid(row=13,column=1)
    

    root.mainloop()



#deactivate()
