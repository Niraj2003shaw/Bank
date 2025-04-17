import tkinter as tk
import Activate_tk as attk
import Deactivate_tk as dttk
import date_tk as datk
import day_to_day_tk as dayttk


def admin_work():
    
    def act_tk():
        attk.activate()


    def deact_tk():
        dttk.deactivate()

    def da_tk():
        datk.gcal()
    
    def dat_tk():
        dayttk.gcal()
        

    def exit_application():
        root.destroy()

    root = tk.Tk()
    root.title("NBI NATIONAL BANK")

    # Create main frame
    main_frame = tk.Frame(root, bg="green")
    main_frame.pack(padx=20, pady=20)

    # Create title label
    title_label = tk.Label(main_frame, text="Welcome User", font=("Arial", 24), bg="red",fg="black")
    title_label.pack(pady=20)

    # Create buttons frame
    buttons_frame = tk.Frame(main_frame, bg="#f0f0f0")
    buttons_frame.pack(pady=20)

    # Create buttons
    new_user_button = tk.Button(buttons_frame, text=" ACTIVATE ", font=("Arial", 16),fg="brown" ,width=15, height=2,bg="white",command=act_tk)
    new_user_button.pack(side=tk.LEFT, padx=10)

    new_user_button1 = tk.Button(buttons_frame, text=" DE-ACTIVATE ", font=("Arial", 16),fg="brown" ,width=15, height=2,bg="white",command=deact_tk)
    new_user_button1.pack(side=tk.LEFT, padx=10)

    existing_user_button = tk.Button(buttons_frame, text=" TODAY'S REC ", font=("Arial", 16),fg="brown", width=15, height=2,bg="white",command=da_tk)
    existing_user_button.pack(side=tk.LEFT, padx=10)

    existing_user_button1 = tk.Button(buttons_frame, text=" DAY-TO-DAY REC ", font=("Arial", 16),fg="brown", width=15, height=2,bg="white",command=dat_tk)
    existing_user_button1.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(buttons_frame, text="Exit", command=exit_application, font=("Arial", 16),fg="brown", width=15, height=2,bg="white")
    exit_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()


#admin_work()
