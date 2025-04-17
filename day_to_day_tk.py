import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime, date
import datetime
import mysql.connector


dd =''
def gcal():

    
    def calendar():
        
        def get_date():
            try:
                global dd
                formatted_date, formatted_date1 = '', ''
                date = cal.selection_get()
                if dd == '':
                    formatted_date = date.strftime("%Y-%m-%d")
                    dd = formatted_date
                    text_box.delete(1.0, tk.END)
                    text_box.insert(tk.END, formatted_date)
                else:
                    formatted_date1 = date.strftime("%Y-%m-%d")
                    text_box.delete(1.0, tk.END)
                    text_box.insert(tk.END, formatted_date1)
                
                # Create a connection to the database
                mycon = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    passwd="1234",
                    database="niraj"
                )
                mycon.autocommit = True
                cursor = mycon.cursor()
                # Execute the SQL query
                
                if(dd != '' and formatted_date1 != ''):
                    
                    query = "SELECT ddate,amt FROM deposit WHERE ddate BETWEEN %s AND %s"
                    cursor.execute(query, (formatted_date, formatted_date1))
                    
                    # Fetch the results
                    m = []
                    ld = []
                    sumd = 0
                    for row in cursor:
                        #print(row)
                        dt=row[0]
                        m.append(dt)
                        m.append(row[1])
                        sumd += m[1]
                        m.append("D")
                        ld.append(m)
                        m = []
                    ld.append(sumd)
                        #sumd = 0
                    #print(ld,sumd)
                    
                    # Insert the values into the text boxes
                    text_box2.delete(1.0, tk.END)
                    for data in range(len(ld) - 1):
                        if isinstance(ld[data], list):  # Check if ld[data] is a list
                            text_box2.insert(tk.END, str(ld[data][0])+',')
                            text_box2.insert(tk.END, str(ld[data][1])+',')
                            text_box2.insert(tk.END, str(ld[data][2]))
                            text_box2.insert(tk.END, '\n')
                        else:
                            text_box2.insert(tk.END, str(ld[data]))  # Convert to string
                            text_box2.insert(tk.END, '\n')
                    text_box3.insert(tk.END, str(ld[len(ld) - 1]))
                    
                    # Close the database connection
                    #mycon.close()
            #except mysql.connector.Error as err:
                #print("Error: {}".format(err))
            
         


                if(dd != '' and formatted_date1 != ''):
                        query = "SELECT wdate,amt FROM withdrew WHERE wdate BETWEEN %s AND %s"
                        cursor.execute(query, (formatted_date, formatted_date1))
                            
                            # Fetch the results
                        m = []
                        ld = []
                        sumd = 0
                        for row in cursor:
                            dt=row[0]
                            m.append(dt)
                                #print(row)
                            m.append(float(row[1]))
                            sumd += m[1]
                            m.append("W")
                            ld.append(m)
                            m = []
                        ld.append(sumd)
                                #sumd = 0
                        #print(ld,sumd)
                            
                            # Insert the values into the text boxes
                        text_box1.delete(1.0, tk.END)
                        for data in range(len(ld) - 1):
                            if isinstance(ld[data], list):  # Check if ld[data] is a list
                                text_box1.insert(tk.END, str(ld[data][0])+',')
                                text_box1.insert(tk.END, str(ld[data][1])+',')
                                text_box1.insert(tk.END, str(ld[data][2]))
                                text_box1.insert(tk.END, '\n')
                            else:
                                text_box1.insert(tk.END, str(ld[data]))  # Convert to string
                                text_box1.insert(tk.END, '\n')
                        text_box4.insert(tk.END, str(ld[len(ld) - 1]))
                            
                            # Close the database connection
                        mycon.close()
            except mysql.connector.Error as err:
                print("Error: {}".format(err))
            

            
            
            
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

    
    store_button = tk.Button(main_frame,text=" FROM ",font=("Arial Black", 8, "bold"),fg="#E3979A",bg="black",relief=tk.RIDGE,width=8,height=2,command=calendar)
    store_button.grid(row=0,column=1)
    
    store_button = tk.Button(main_frame,text=" TO ",font=("Arial Black", 8, "bold"),fg="#E3979A",bg="black",relief=tk.RIDGE,width=8,height=2,command=calendar)
    store_button.grid(row=0,column=2)

    name_label = tk.Label(main_frame,text=" WITHDREW ",fg="#E3979A")
    name_label.grid(row=2,column=0)

    text_box1 = tk.Text(main_frame,height=8,width=40)
    text_box1.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box1.yview)
    text_box1.grid(row=2,column=1,columnspan=2)
    scrollbar.grid(row=2,column=2,sticky="ns")

    name_label = tk.Label(main_frame,text=" DEPOSIT ",fg="#E3979A")
    name_label.grid(row=3,column=0)

    text_box2 = tk.Text(main_frame,height=8,width=40)
    text_box2.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box2.yview)
    text_box2.grid(row=3,column=1,columnspan=2)
    scrollbar.grid(row=3,column=2,sticky="ns")

    name_label = tk.Label(main_frame,text=" TOTAL DEPOSIT ",fg="#E3979A")
    name_label.grid(row=4,column=0)

    text_box3 = tk.Text(main_frame,height=2,width=12)
    text_box3.grid(row=4,column=1,columnspan=2)

    name_label = tk.Label(main_frame,text=" TOTAL WITHDTEW ",fg="#E3979A")
    name_label.grid(row=5,column=0)

    text_box4 = tk.Text(main_frame,height=2,width=12)
    text_box4.grid(row=5,column=1,columnspan=2)
    

    store_button = tk.Button(main_frame,text=" DONE ",font=("Arial Black", 8, "bold"),fg="#E3979A",bg="black",relief=tk.RIDGE,width=8,height=2,command=close)
    store_button.grid(row=6,column=2)

    root1.mainloop
    
    


#gcal()
