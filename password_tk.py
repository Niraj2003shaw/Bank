import tkinter as tk
from tkinter import messagebox
from tkinter import Entry

pp=""

def pass_create():
    def verify(n,n1):
        c,c1,c2,c3=0,0,0,0
        if len(n)<8 or len(n)>10:
            return 0
        if n.count(' ')>0:
            return 0
        for i in n:
            if ord(i)>64 and ord(i)<91:
                c1=c1+1
            if ord(i)>96 and ord(i)<123:
                c2=c2+1
            if  ord(i)>=48 and ord(i)<=57:
                c=c+1
            else:
                c3=c3+1
            
        if c==0 or c1==0 or c2==0 or c3==0 or n!=n1:
            return 0
        return 1
                
    def check():
        global pp
        input_pass = text_box1.get()

        input_cpass = text_box2.get()        

        if(verify(input_pass,input_cpass)==0):
            messagebox.showinfo("Error!","Password Not Correct")
            pp="not"
            return (pp)
        pp=input_pass
        return (pp)


    root = tk.Tk()
    root.title("Password Creation")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text="PASSWORD",fg="#507d2a")
    name_label.grid(row=1,column=0)

    text_box1 = Entry(main_frame,bd=8,width=35,show="*")
    text_box1.grid(row=1,column=1)

    name_label = tk.Label(main_frame,text="CONFIRM PASS",fg="#507d2a")
    name_label.grid(row=3,column=0)

    text_box2 = Entry(main_frame,bd=8,width=35,show="*")
    text_box2.grid(row=3,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=check)
    store_button.grid(row=4,column=1)
    
    
    

    root.mainloop()
    
    return (pp)
    

    



