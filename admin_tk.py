import tkinter as tk


def admin_manage():

    root = tk.Tk()
    root.title("Bank Maneger")

    main_frame = tk.Frame(root)
    main_frame.pack()

    store_button = tk.Button(main_frame,text="   ACTIVATE    ",font=("Arial Black", 15 , "bold"),fg="red",bg="yellow",relief=tk.RIDGE,width=10,height=2)
    store_button.grid(row=0,column=1)

    store_button = tk.Button(main_frame,text="   DEACTIVATE    ",font=("Arial Black", 15 , "bold"),fg="red",bg="yellow",relief=tk.RIDGE,width=11,height=2)
    store_button.grid(row=1,column=1)

    store_button = tk.Button(main_frame,text=" TODAY'S RECORD ",font=("Arial Black", 15, "bold"),fg="red",bg="yellow",relief=tk.RIDGE,width=15,height=2)
    store_button.grid(row=4,column=1)

    store_button = tk.Button(main_frame,text=" DATE-TO-DATE ",font=("Arial Black", 15, "bold"),fg="red",bg="yellow",relief=tk.RIDGE,width=12,height=2)
    store_button.grid(row=2,column=1)

    


    root.mainloop()




admin_manage()
