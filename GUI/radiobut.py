import tkinter
from tkinter import *

root1=Tk()
def lol():
        def sel():
                selection=str(var.get())
                print(selection)

        var = StringVar()

        myradio = Radiobutton(root1, text="Male", value="Male", variable=var, command=sel).grid(row=3, column=1)
        myradio1 = Radiobutton(root1, text="Female", value="female", variable=var, command=sel).grid(row=3, column=2)



lol()
root1.mainloop()