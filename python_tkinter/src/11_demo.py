from tkinter import *

root = Tk()

canvas = Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 50, 100)
otherline = canvas.create_line(10, 10, 1000, 1000, fill="Green")

root.mainloop()
