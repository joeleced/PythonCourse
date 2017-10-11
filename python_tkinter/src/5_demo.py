from tkinter import *

root = Tk()

def dosomething():
    print("Button clicked")

button1 = Button(root,text="Button1",command=dosomething).pack()


root.mainloop()