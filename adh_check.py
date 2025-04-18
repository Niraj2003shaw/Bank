import tkinter as tk
from tkinter import messagebox
from datetime import date
from dateutil import parser





def adhar_check(n):
    if(len(n.strip())==12):
        messagebox.showinfo("OKAY!","Your Ahar Accepted")
    else:
        messagebox.showinfo("Error!","Wrong Adhar No.")
        
    
   
def pan_check(n):
    
    n=n.strip()
    if(n.isalnum() and len(n)==10 ):
        if(n[5:9].isdigit()):
            messagebox.showinfo("OKAY!","Your PAN Accepted")
        else:
            messagebox.showinfo("ERROR!","Your PAN NOT Accepted") 
    else:
        messagebox.showinfo("ERROR!","Your PAN NOT Accepted")


    
    

def dat_check(n):
    #n=n.strip()
    n1=str(date.today())
    if((parser.parse(n1)-parser.parse(n)).days/365 >= 18):
        messagebox.showinfo("OKAY!","You are eligible")
    else:
        messagebox.showinfo("ERROR!","Your not eligible")

    


