from tkinter import *
from tkinter import messagebox

window = Tk()
window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
window.withdraw()

messagebox.showinfo('Error', 'Invalid Name')

window.deiconfy()
window.destroy()
window.quit()