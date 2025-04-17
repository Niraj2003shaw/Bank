import tkinter as tk
import adh_check as ac
import entry_tk as et
import password_tk as pt
import random

def new_detail():
    
    def store_name():
        pass1="nj"
        input_name = text_box1.get("1.0",tk.END)
        
        
        input_fname = text_box2.get("1.0",tk.END)
        
        
        input_add1 = text_box3.get("1.0",tk.END)
        
        
        input_add2 = text_box4.get("1.0",tk.END)
        
        
        input_lm = text_box5.get("1.0",tk.END)
        

        input_city = text_box6.get("1.0",tk.END)
        
        
        input_pin = text_box7.get("1.0",tk.END)
        
        
        input_mob = text_box8.get("1.0",tk.END)
        
        
        input_dob = text_box9.get("1.0",tk.END)
        ac.dat_check(input_dob)
        
        
        input_email = text_box10.get("1.0",tk.END)
        
        
        input_gen = text_box11.get("1.0",tk.END)
        
        
        input_adh = text_box12.get("1.0",tk.END)
        ac.adhar_check(input_adh)
        
        
        input_pan = text_box13.get("1.0",tk.END)
        ac.pan_check(input_pan.strip())

        #l=[]

        
        acno=random.randint(10**(5),(10**6)-1)
        #l.append(acno)
        #if acno in l:
            #acno=random.randint(10**(5),(10**6)-1)

        pass1 = pt.pass_create()
        
                
        if(pass1!='not'):
            et.entry_det(acno,input_name.strip(),input_fname.strip(),input_add1.strip(),input_add2.strip(),input_lm.strip(),input_city.strip(),input_pin.strip(),input_mob.strip(),input_dob.strip(),\
                      input_email.strip(),input_gen.strip(),pass1,input_pan.strip(),input_adh.strip())
        
        
        


    
    root = tk.Tk()
    root.title("Customer Detail")

    main_frame = tk.Frame(root)
    main_frame.pack()

    name_label = tk.Label(main_frame,text="Customer Name",fg="red")
    name_label.grid(row=0,column=0)

    text_box1 = tk.Text(main_frame,height=2,width=30)
    text_box1.grid(row=0,column=1)
    #text_box.pack(row=0,column=0,side=tk.RIGHT)

    fname_label = tk.Label(main_frame,text="Customer Gaurdian Name",fg="red")
    fname_label.grid(row=1,column=0)


    text_box2 = tk.Text(main_frame,height=2,width=30)
    text_box2.grid(row=1,column=1)
    #text_box.pack(row=1,column=0,side=tk.RIGHT)

    fname_label = tk.Label(main_frame,text="Address 1",fg="red")
    fname_label.grid(row=2,column=0)
    

    text_box3 = tk.Text(main_frame,height=2,width=30)
    text_box3.grid(row=2,column=1)
     
    fname_label = tk.Label(main_frame,text="Address 2",fg="red")
    fname_label.grid(row=3,column=0)
    

    text_box4 = tk.Text(main_frame,height=2,width=30)
    text_box4.grid(row=3,column=1)

    fname_label = tk.Label(main_frame,text="Landmark ",fg="red")
    fname_label.grid(row=4,column=0)
    

    text_box5 = tk.Text(main_frame,height=2,width=30)
    text_box5.grid(row=4,column=1)

    fname_label = tk.Label(main_frame,text="City",fg="red")
    fname_label.grid(row=5,column=0)
    

    text_box6 = tk.Text(main_frame,height=2,width=30)
    text_box6.grid(row=5,column=1)

    fname_label = tk.Label(main_frame,text="Pin Code ",fg="red")
    fname_label.grid(row=6,column=0)
    

    text_box7 = tk.Text(main_frame,height=2,width=30)
    text_box7.grid(row=6,column=1)

    fname_label = tk.Label(main_frame,text="Mobile No.",fg="red")
    fname_label.grid(row=7,column=0)
    

    text_box8 = tk.Text(main_frame,height=2,width=30)
    text_box8.grid(row=7,column=1)
    
    fname_label = tk.Label(main_frame,text="Date-of-Birth ",fg="red")
    fname_label.grid(row=8,column=0)
    

    text_box9 = tk.Text(main_frame,height=2,width=30)
    text_box9.grid(row=8,column=1)

    fname_label = tk.Label(main_frame,text="Email",fg="red")
    fname_label.grid(row=9,column=0)
    

    text_box10 = tk.Text(main_frame,height=2,width=30)
    text_box10.grid(row=9,column=1)

    fname_label = tk.Label(main_frame,text="Gender",fg="red")
    fname_label.grid(row=10,column=0)
    

    text_box11 = tk.Text(main_frame,height=2,width=30)
    text_box11.grid(row=10,column=1)
    
    fname_label = tk.Label(main_frame,text="Adhar No.",fg="red")
    fname_label.grid(row=11,column=0)
    

    text_box12 = tk.Text(main_frame,height=2,width=30)
    text_box12.grid(row=11,column=1)

    fname_label = tk.Label(main_frame,text="PAN No.",fg="red")
    fname_label.grid(row=12,column=0)
    

    text_box13 = tk.Text(main_frame,height=2,width=30)
    text_box13.grid(row=12,column=1)

    store_button = tk.Button(main_frame,text="SUBMIT",command=store_name)
    store_button.grid(row=13,column=1)




    root.mainloop()

#new_detail()
