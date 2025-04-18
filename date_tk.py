import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from datetime import date
import mysql.connector
import tkinter.scrolledtext as scrolledtext 



mycon=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="niraj")
mycon.autocommit=True
cursor=mycon.cursor()

s='use niraj'
cursor.execute(s)


def gcal():
    
    def calendar():
        
        
        def get_date():
            global dd
            m=[]
            ld=[]
            lw=[]
            sumd=0
            date = cal.selection_get()
            formatted_date = date.strftime("%Y-%m-%d")
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END,formatted_date )
            #print(formatted_date,type(formatted_date))
            
            
            cursor.execute("select amt from deposit where ddate = '{}'".format(formatted_date))
            #text_box1.delete(1.0, tk.END)
            for row in cursor:
                m.append(row[0])
                sumd = m[0]+sumd
                ld.append(m)
                m=[]
            ld.append(sumd)
            #print(ld)
            sumd = 0
            for data in range(len(ld)-1):
                text_box2.insert(tk.END,ld[data][0])
                text_box2.insert(tk.END,'\n')
            text_box3.insert(tk.END,ld[len(ld)-1])

            cursor.execute("select amt from withdrew where wdate = '{}'".format(formatted_date))

            for row in cursor:
                m.append(float(row[0]))
                sumd = m[0]+sumd
                lw.append(m)
                m=[]
            lw.append(sumd)
            #print(lw)
            sumd = 0
            for data in range(len(lw)-1):
                text_box1.insert(tk.END,lw[data][0])
                text_box1.insert(tk.END,'\n')
            text_box4.insert(tk.END,lw[len(lw)-1])
            
            

            
            
            
        def close():
            root.destroy()

            
        root = tk.Tk()
        root.title("CALENDAR")
        
        
        
        
        sub_frame = tk.Frame(root)
        sub_frame.grid(row=0, column=0, padx=10, pady=10)
        

        today = str(date.today())
        today = today.split('-')

        cal = Calendar(sub_frame, selectmode='day', year=int(today[0]), month=int(today[1]), day=int(today[2]))
        cal.grid(row=0, column=0, columnspan=2)


        store_button = tk.Button(sub_frame,text=" GET DATE ",font=("Arial Black", 8, "bold"),fg="black",bg="blue",relief=tk.RIDGE,width=8,height=2,command=get_date)
        store_button.grid(row=1, column=0, columnspan=2)

        label = tk.Label(sub_frame, text="Selected Date:")
        label.grid(row=2, column=0)

        text_box = tk.Text(sub_frame, width=10, height=2)
        text_box.grid(row=2, column=0, columnspan=2)
        
        
        
        store_button = tk.Button(sub_frame,text=" DONE ",font=("Arial Black", 8, "bold"),fg="black",bg="blue",relief=tk.RIDGE,width=8,height=2,command=close)
        store_button.grid(row=5, column=0, columnspan=2)


        root.mainloop()




    def close():
        root1.destroy()
    
    root1 = tk.Tk()
    root1.title("Bank Maneger")

    main_frame = tk.Frame(root1)
    main_frame.grid(row=0, column=0, padx=10, pady=10)

    scrollbar = tk.Scrollbar(main_frame)
    scrollbar1 = tk.Scrollbar(main_frame)

    
    store_button = tk.Button(main_frame,text=" GET DATE ",font=("Arial Black", 8, "bold"),fg="#FFA000",bg="red",relief=tk.RIDGE,width=8,height=2,command=calendar)
    store_button.grid(row=0,column=1)
    

    name_label = tk.Label(main_frame,text=" WITHDREW ",fg="#FFA000")
    name_label.grid(row=2,column=0)

    text_box1 = tk.Text(main_frame,height=8,width=40)
    text_box1.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box1.yview)
    text_box1.grid(row=2,column=1,columnspan=2)
    scrollbar.grid(row=2,column=2,sticky="ns")

    name_label = tk.Label(main_frame,text=" DEPOSIT ",fg="#FFA000")
    name_label.grid(row=3,column=0)

    text_box2 = tk.Text(main_frame,height=8,width=40)
    text_box2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box2.yview)
    text_box2.grid(row=3,column=1,columnspan=2)
    scrollbar.grid(row=3,column=2,sticky="ns")

    name_label = tk.Label(main_frame,text=" TOTAL DEPOSIT ",fg="#FFA000")
    name_label.grid(row=4,column=0)

    text_box3 = tk.Text(main_frame,height=2,width=12)
    text_box3.grid(row=4,column=1,columnspan=2)

    name_label = tk.Label(main_frame,text=" TOTAL WITHDTEW ",fg="#FFA000")
    name_label.grid(row=5,column=0)

    text_box4 = tk.Text(main_frame,height=2,width=12)
    text_box4.grid(row=5,column=1,columnspan=2)
    

    store_button = tk.Button(main_frame,text=" DONE ",font=("Arial Black", 8, "bold"),fg="#FFA000",bg="red",relief=tk.RIDGE,width=8,height=2,command=close)
    store_button.grid(row=6,column=2)

    root1.mainloop
    
    


#gcal()
