from tkinter import *
from functools import partial
from time import sleep

def openApp():
    sleep(0.2)
    tkWarning.destroy()
    import app
    newWindow = Toplevel(app.py)

def cancelApp():
    sleep(0.2)
    tkWarning.destroy()

#widnow
tkWarning = Tk() 
windowWidth = tkWarning.winfo_reqwidth()
windowHeight = tkWarning.winfo_reqheight()

tkWarning.geometry('450x110')  
tkWarning.title('Warning')
tkWarning.resizable(False, False)

windowWidth = tkWarning.winfo_reqwidth()
windowHeight = tkWarning.winfo_reqheight()

positionRight = int(tkWarning.winfo_screenwidth()/2+(-60) - windowWidth/2+(-60))
positionDown = int(tkWarning.winfo_screenheight()/2 - windowHeight/2)

tkWarning.geometry("+{}+{}".format(positionRight, positionDown))

lbl1 = usernameLabel = Label(tkWarning, text="What are you going to witness may affect you emotionally\nDo you want to continue?")
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl1.pack()


#login button
#command=
lbl2 = yesButton = Button(tkWarning, text="Ok", command = openApp)
lbl2.place(relx = 0.7, rely = 0.5, anchor=CENTER)

lbl3 = noButton = Button(tkWarning, text="Cancel", command = cancelApp)
lbl3.place(relx = 0.3, rely = 0.5, anchor=CENTER)

tkWarning.mainloop()