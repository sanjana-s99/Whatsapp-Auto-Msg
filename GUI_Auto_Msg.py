from selenium import webdriver
from tkinter import *
import tkinter as tk  
from functools import partial
from tkinter import messagebox  

def verify(n1, n2, n3):
    name = (n1.get())  
    msg = (n2.get())
    count = (n3.get()) 

    a=len(name)
    b=len(msg)
    c=len(count)
    print("To : "+name)
    print("Message : "+msg)
    print(count+" messages.")

    if a==0 or b==0 or c==0:
        messagebox.showerror("Error","Error!! Please Re-Check Your Entered Data")
    else:
        messagebox.showinfo("Verifyed","Scan QR To Login And Hit Send...") 

def send_msg(n1, n2, n3): 
    name = (n1.get())  
    msg = (n2.get())
    count = (n3.get()) 
    user = driver.find_element_by_xpath("//span[@title = '{}']".format(name))
    user.click()
    msg_box = driver.find_element_by_class_name("_13mgZ")
    for i in range(int(count)):
        print(str(i+1) + " " + msg)
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name("_3M-N-")
        button.click()
    a=("Scan QR To Login And Hit Send..." + count + "Messages.")
    messagebox.showinfo("Done!", a) 
 
   
root = tk.Tk() 
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com') 
root.title('Whatsapp Auto')  
   
number1 = tk.StringVar()  
number2 = tk.StringVar()  
number3 = tk.StringVar() 
  
labelNum1 = tk.Label(root, text="Name of user or group :").grid(row=1, column=0)  
labelNum2 = tk.Label(root, text="Message : ").grid(row=2, column=0) 
labelNum3 = tk.Label(root, text="Message Count : ").grid(row=3, column=0)  
  
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)  
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
entryNum3 = tk.Entry(root, textvariable=number3).grid(row=3, column=2)  
  
send_msg = partial(send_msg, number1, number2, number3) 
verify = partial(verify, number1, number2, number3)

buttonCa1 = tk.Button(root, text="Verify", command=verify,activeforeground = "blue",activebackground = "aqua",pady=5).grid(row=4, column=0) 
buttonCa2 = tk.Button(root, text="Send", command=send_msg,activeforeground = "red",activebackground = "pink",pady=5).grid(row=4, column=2)  

root.mainloop()  

