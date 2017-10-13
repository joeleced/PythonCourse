from tkinter import *
import tkinter.messagebox

# root = Tk()
tkinter.messagebox.showinfo("Title", "Message man")

response = tkinter.messagebox.askquestion("Question Time", "Was Jimmy ur dog")
if response == "yes":
    print("Yes It is")
else:
    print("Nope its not")

# root.mainloop()