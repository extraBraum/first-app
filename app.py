import winsound
from tkinter import *
from functools import partial

winsound.PlaySound('melodie.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

tkApp = Tk() 
windowWidth = tkApp.winfo_reqwidth()
windowHeight = tkApp.winfo_reqheight()

tkApp.geometry('1x1')  
tkApp.title('Truth speaker')
tkApp.resizable(False, False)


windowWidth = tkApp.winfo_reqwidth()
windowHeight = tkApp.winfo_reqheight()

positionRight = int(tkApp.winfo_screenwidth()/2+(-6000) - windowWidth/2+(-6000))
positionDown = int(tkApp.winfo_screenheight()/2 - windowHeight/2)

tkApp.geometry("+{}+{}".format(positionRight, positionDown))

tkApp.overrideredirect(True)

tkApp.mainloop()