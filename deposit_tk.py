import tkinter as tk
from datetime import date
import entry_depo as ed

def depo_tk():


    def entry_depo():
        input_ac = text_box1.get("1.0",tk.END)

        input_amt = text_box2.get("1.0",tk.END)

        input_rem = text_box3.get("1.0",tk.END)
        

        ddate = date.today()
        root.destroy()

        ed.entry_det(int(input_ac.strip()),ddate,int(input_amt.strip()),input_rem.strip())


    root = tk.Tk()
    root.title("DEPOSIT")

    main_frame = tk.Frame(root)
    main_frame.pack()
    

    name_label = tk.Label(main_frame,text=" A/C Number ",fg="maroon")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)
    
    

    name_label = tk.Label(main_frame,text=" Amount ",fg="maroon")
    name_label.grid(row=1,column=0)

    text_box2 = tk.Text(main_frame,height=2,width=30)
    text_box2.grid(row=1,column=1)

    name_label = tk.Label(main_frame,text=" Remarks ",fg="maroon")
    name_label.grid(row=2,column=0)

    text_box3 = tk.Text(main_frame,height=2,width=30)
    text_box3.grid(row=2,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=entry_depo)
    store_button.grid(row=13,column=1)
    

    root.mainloop()






#depo_tk()
 
