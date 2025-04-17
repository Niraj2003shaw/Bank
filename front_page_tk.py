import tkinter as tk
import details_tk as dtk
import existing_tk as extk
import adminfront_tk as adtk


def new_user():
    dtk.new_detail()

def exist_tk():
    extk.existing_user()

def admin_tk():
    adtk.admin_work()

def exit_application():
    root.destroy()

root = tk.Tk()
root.title("NBI NATIONAL BANK")

# Create main frame
main_frame = tk.Frame(root, bg="yellow")
main_frame.pack(padx=20, pady=20)

# Create title label
title_label = tk.Label(main_frame, text="Welcome to Our Bank", font=("Arial", 24), bg="#800080")
title_label.pack(pady=20)

# Create buttons frame
buttons_frame = tk.Frame(main_frame, bg="#f0f0f0")
buttons_frame.pack(pady=20)

# Create buttons
new_user_button = tk.Button(buttons_frame, text="New User", command=new_user, font=("Arial", 16),fg="red" ,width=15, height=2,bg="#800080")
new_user_button.pack(side=tk.LEFT, padx=10)

existing_user_button = tk.Button(buttons_frame, text="Existing User",command=exist_tk, font=("Arial", 16),fg="red", width=15, height=2,bg="#800080")
existing_user_button.pack(side=tk.LEFT, padx=10)

admin_button = tk.Button(buttons_frame, text=" ADMIN ",command=admin_tk, font=("Arial", 16),fg="red", width=15, height=2,bg="#800080")
admin_button.pack(side=tk.LEFT, padx=10)

exit_button = tk.Button(buttons_frame, text="Exit", command=exit_application, font=("Arial", 16),fg="red", width=15, height=2,bg="#800080")
exit_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
