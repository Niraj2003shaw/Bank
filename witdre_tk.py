import tkinter as tk
from datetime import date
from tkinter import Entry
import senpass_tk as spt
import wdamt_tk as wdt
from tkinter import messagebox



def withdrew_tk():

    def wd_ent():
        wdate = date.today()

        input_ac = text_box1.get("1.0",tk.END)

        input_pass = text_box2.get()

        input_cpass = text_box3.get()

        password = spt.passes_tk(input_ac.strip())
        root.destroy()

        if (input_pass.strip()==input_cpass.strip() and password == input_pass.strip()):
            wdt.withamt(int(input_ac.strip()),wdate)
        else:
            messagebox.showinfo("ERROR!","Password not match")

          

        


    root = tk.Tk()
    root.title("WITHDRAWAL")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" A/C Number ",fg="purple")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)

    name_label = tk.Label(main_frame,text="PASSWORD",fg="purple")
    name_label.grid(row=1,column=0)

    text_box2 = Entry(main_frame,bd=8,width=35,show="*")
    text_box2.grid(row=1,column=1)

    name_label = tk.Label(main_frame,text="CONFIRM PASS",fg="purple")
    name_label.grid(row=3,column=0)

    text_box3 = Entry(main_frame,bd=8,width=35,show="*")
    text_box3.grid(row=3,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=wd_ent)
    store_button.grid(row=13,column=1)

    

    root.mainloop()







#withdrew_tk()
