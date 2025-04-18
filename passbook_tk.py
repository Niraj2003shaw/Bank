import tkinter as tk
import mysql.connector
import add_tk as adw

def passbk():

    def printpb():
        input_ac = text_box1.get("1.0",tk.END)
        root.destroy()
        l=[]
        l= adw.add_dep_with(input_ac)
        cb = adw.add_cb(input_ac)


        adw.display_pb(l,cb)
        #print(l)
        #print(cb)
        
        

    root = tk.Tk()
    root.title("PASSBOOK ")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text=" A/C ",fg="orange")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=printpb)
    store_button.grid(row=13,column=1)



    root.mainloop()



#passbk()
