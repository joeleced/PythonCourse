from tkinter import *


def printfunc():
    print("Submenu Clicked")


root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

submenu = Menu(menubar)

menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Project", command=printfunc)
submenu.add_command(label="Save", command=printfunc)

submenu.add_separator()
submenu.add_command(label="Exit", command=printfunc)

newmenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Cut", command=printfunc)

toolbar = Frame(root, bg="pink")
button1 = Button(toolbar, text="Paste", command=printfunc)
button1.pack(side=LEFT, padx=3, pady=4)

button2 = Button(toolbar, text="Undo", command=printfunc)
button2.pack(side=LEFT, padx=3, pady=4)

toolbar.pack(side=TOP, fill=X)

statusbar = Label(root, text="This is the status", bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
