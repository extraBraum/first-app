from tkinter import *
from functools import partial
from time import sleep

def openLoading():
    while True:
        if not usernameEntry.get():
            import loginError
            errorWindow = TopLevel(loginError.py)
        else:
            tkWindow.destroy()
            sleep(0.6)
            import loadingScreen
            newWindow = Toplevel(loadingScreen.py)

#widnow
tkWindow = Tk() 
windowWidth = tkWindow.winfo_reqwidth()
windowHeight = tkWindow.winfo_reqheight()

tkWindow.geometry('400x150')  
tkWindow.title('Truth speaker')
tkWindow.resizable(False, False)

windowWidth = tkWindow.winfo_reqwidth()
windowHeight = tkWindow.winfo_reqheight()

positionRight = int(tkWindow.winfo_screenwidth()/2+(-60) - windowWidth/2+(-60))
positionDown = int(tkWindow.winfo_screenheight()/2 - windowHeight/2)

tkWindow.geometry("+{}+{}".format(positionRight, positionDown))

tkWindow.iconbitmap(default='transparent.ico')


#username label and text box
lbl1 = usernameLabel = Label(tkWindow, text="\nEnter your name:")
lbl1.place(relx=0.5, rely=0.5, anchor=CENTER)
lbl1.pack()
username = StringVar()
txtbox = usernameEntry = Entry(tkWindow, textvariable=username)
txtbox.pack()
txtbox.place(relx = 0.5, rely = 0.4, anchor = CENTER)

#login button
#command=
lbl2 = loginButton = Button(tkWindow, text="Submit", command = openLoading)
lbl2.place(relx = 0.5, rely = 0.6, anchor=CENTER)

tkWindow.mainloop()