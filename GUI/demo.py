from tkinter import *

def newwindow():
    root1=Tk()

root=Tk()

root.title("My Window")
root.minsize(200,200)
root.maxsize(300,300)
mylabel=Label(root,text="This is shit",bg='black',fg='white')
mylabel.pack()
mybutton=Button(root,text='Click me',command=newwindow)
mybutton.pack()

myinput=Entry(root).pack()
x=IntVar()
myradio=Radiobutton(root, text='Ans 1',variable=x,value=1).pack()
myradio1=Radiobutton(root, text='Ans 3',variable=x,value=2).pack()
myradio2=Radiobutton(root, text='Ans 4',variable=x,value=3).pack()
mycheck=Checkbutton(root, text='Ans 2').pack()
print(x.get())
root.mainloop()