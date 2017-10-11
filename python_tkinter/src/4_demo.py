from tkinter import *
root = Tk()

label1 = Label(root, text="First", bg="Blue", fg="Red")
label1.pack(fill=X)

label2 = Label(root, text="Second", bg="Red", fg="Blue")
label2.pack(side=LEFT,fill=Y)

root.mainloop()