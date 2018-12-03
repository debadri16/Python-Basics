from tkinter import *
root=Tk()
root.title('my window')
root.maxsize(300,300)
root.minsize(200,200)
emaillabel=Label(root,text='Email: ')
emaillabel.grid(row=0,column=0)
emailInput=Entry(root)
emailInput.grid(row=0,column=1)

passwordlabel=Label(root,text='Password: ')
passwordlabel.grid(row=1,column=0)
passwordinput=Entry(root)
passwordinput.grid(row=1,column=1)

submitbutton=Button(root,text="Login")
submitbutton.grid(row=2,column=1)

root.mainloop()