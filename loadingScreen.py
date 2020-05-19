import tkinter as tk
from tkinter import *
from functools import partial
from tkinter.ttk import *
from time import sleep
from tkinter import ttk
from tkinter.ttk import *

def bar(): 
    import time 
    progress['value'] = 5
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 10
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 15
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 20
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 25
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
    
    progress['value'] = 30
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 35
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 40
    tkLoading.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 45
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 50
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
    progress['value'] = 55

    progress['value'] = 60
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 65
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 70
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 75
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 80
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
    
    progress['value'] = 85
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 90
    tkLoading.update_idletasks() 
    time.sleep(0.5) 
  
    progress['value'] = 95
    tkLoading.update_idletasks() 
    time.sleep(1) 
  
    progress['value'] = 100
    tkLoading.update_idletasks() 
    time.sleep(0.5) 

def openmodule1():
    tkLoading.destroy()
    sleep(0.6)
    import warning
    newWindow = Toplevel(warning.py)

tkLoading = tk.Tk() 
windowWidth = tkLoading.winfo_reqwidth()
windowHeight = tkLoading.winfo_reqheight()

tkLoading.geometry('400x150')  
tkLoading.title('Loading...')
tkLoading.resizable(False, False)

windowWidth = tkLoading.winfo_reqwidth()
windowHeight = tkLoading.winfo_reqheight()

positionRight = int(tkLoading.winfo_screenwidth()/2+(-60) - windowWidth/2+(-60))
positionDown = int(tkLoading.winfo_screenheight()/2 - windowHeight/2)

tkLoading.geometry("+{}+{}".format(positionRight, positionDown))

prb = progress = Progressbar(tkLoading, orient = HORIZONTAL, length = 350, mode = 'determinate')
prb.place(relx = 0.5, rely = 2, anchor = CENTER)

lbl1 = usernameLabel = Label(tkLoading, text="\nPlease wait.")
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl1.pack()
lbl1 = usernameLabel = Label(tkLoading, text="")
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl1.pack()
lbl1 = usernameLabel = Label(tkLoading, text="")
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl1.pack()
  
progress.pack(pady = 10)

tkLoading.after(2000, bar)

tkLoading.after(2000, openmodule1)

tkLoading.mainloop()