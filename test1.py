import random
import string
from tkinter import *

root = Tk()

def addCheckBox():
    checkBoxName = "".join(str(random.random()) for _ in range(1))
    c = Checkbutton(root, text=checkBoxName)
    c.pack()

b = Button(root, text="Add a checkbox", command=addCheckBox)
b.pack()

premadeList = ["foo", "bar", "baz"]

for checkBoxName in premadeList:
    c = Checkbutton(root, text=checkBoxName)
    c.pack()

root.mainloop()