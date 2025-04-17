import tkinter as tk
import mysql.connector
from tkinter import messagebox


mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)



def activate():
    def ac_activation():
        input_ac = text_box1.get("1.0",tk.END)

        input_mob = text_box2.get("1.0",tk.END)

        input_pan = text_box3.get("1.0",tk.END)

        input_adh = text_box4.get("1.0",tk.END)
        
        root.destroy()

        cursor.execute("select * from cusinfo   where acno={}".format(input_ac.strip()))

        for row in cursor:
            if(row[12] == 'D'):
                cursor.execute("update cusinfo set remark='{}' where acno={} and pan ='{}' and adh ={} and mobileno ={}".format('A',input_ac.strip(),input_pan.strip(),input_adh.strip(),\
                                                                                                                               input_mob.strip()))
                messagebox.showinfo("SUCCESS","You A/C Is Being Activated")
            else:
                messagebox.showinfo("ERROR!","You A/C Is Already Active")

        

    root = tk.Tk()
    root.title("Bank Maneger")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" A/C Number ",fg="#FF007F")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)

    name_label = tk.Label(main_frame,text=" Mobile No. ",fg="#FF007F")
    name_label.grid(row=1,column=0)

    text_box2 = tk.Text(main_frame,height=2,width=30)
    text_box2.grid(row=1,column=1)

    name_label = tk.Label(main_frame,text=" Pan No. ",fg="#FF007F")
    name_label.grid(row=2,column=0)

    text_box3 = tk.Text(main_frame,height=2,width=30)
    text_box3.grid(row=2,column=1)

    name_label = tk.Label(main_frame,text=" Adhaar No. ",fg="#FF007F")
    name_label.grid(row=3,column=0)

    text_box4 = tk.Text(main_frame,height=2,width=30)
    text_box4.grid(row=3,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=ac_activation)
    store_button.grid(row=13,column=1)
    

    root.mainloop()
    



#activate()
