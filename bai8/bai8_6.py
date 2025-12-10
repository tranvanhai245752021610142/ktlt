from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Demo Menu")
root.geometry("400x300")

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

def NewFile():
    messagebox.showinfo("Thông báo", "New File!")

def OpenFile():
    messagebox.showinfo("Thông báo", "Open File!")

def Exit():
    root.quit()

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)

def InsText():
    messagebox.showinfo("Thông báo", "Text!")

def InsPic():
    messagebox.showinfo("Thông báo", "Picture!")

insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=lambda: messagebox.showinfo("Thông báo", "This is a simple example of a menu"))

root.mainloop()
