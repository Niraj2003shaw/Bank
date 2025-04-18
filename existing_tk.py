import tkinter as tk
import deposit_tk as dptk
import witdre_tk as wdtk
import passbook_tk as pstk


def existing_user():
    
    def new_userd():
        dptk.depo_tk()


    def new_userw():
        wdtk.withdrew_tk()

    def new_userp():
        pstk.passbk()
        

    def exit_application():
        root.destroy()

    root = tk.Tk()
    root.title("NBI NATIONAL BANK")

    # Create main frame
    main_frame = tk.Frame(root, bg="blue")
    main_frame.pack(padx=20, pady=20)

    # Create title label
    title_label = tk.Label(main_frame, text="Welcome User", font=("Arial", 24), bg="white",fg="black")
    title_label.pack(pady=20)

    # Create buttons frame
    buttons_frame = tk.Frame(main_frame, bg="#f0f0f0")
    buttons_frame.pack(pady=20)

    # Create buttons
    new_user_button = tk.Button(buttons_frame, text=" DEPOSIT ", font=("Arial", 16),fg="yellow" ,width=15, height=2,bg="green",command=new_userd)
    new_user_button.pack(side=tk.LEFT, padx=10)

    existing_user_button = tk.Button(buttons_frame, text=" WITHDRAWL ", font=("Arial", 16),fg="yellow", width=15, height=2,bg="green",command=new_userw)
    existing_user_button.pack(side=tk.LEFT, padx=10)

    existing_user_button1 = tk.Button(buttons_frame, text=" PASSBOOK", font=("Arial", 16),fg="yellow", width=15, height=2,bg="green",command=new_userp)
    existing_user_button1.pack(side=tk.LEFT, padx=10)

    exit_button = tk.Button(buttons_frame, text="Exit", command=exit_application, font=("Arial", 16),fg="YELLOW", width=15, height=2,bg="green")
    exit_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()


#existing_user()
