from tkinter import *
import math
from math import *

class calculator:
    def __init__(self):
        self.root=Tk()
        self.root.title('Calculator')
        self.text_var=StringVar()

        self.operator=""
        self.root.maxsize(400,370)
        self.result=Entry(self.root,bg='powder blue',textvariable=self.text_var,font=('arial',19,'bold'),insertwidth=4,width="25",bd=20,justify="right")
        self.result.grid(columnspan=6)

        self.btn1=Button(self.root,text='1',bd=8,font=16,bg='gray',fg='White',width=4,height=2, command=lambda:self.get_num('1')).grid(row=1,column=0)
        self.btn2 = Button(self.root, text='2',bd=8, font=16,bg='gray',fg='White',width=4,height=2, command=lambda:self.get_num('2')).grid(row=1,column=1)
        self.btn3 = Button(self.root, text='3',bd=8,font=16,bg='gray',fg='White',width=4,height=2, command=lambda:self.get_num('3')).grid(row=1,column=2)
        self.btnadd = Button(self.root, text='+',bd=8,font=16, bg='dark gray',fg='black', width=4, height=2, command=lambda:self.get_num('+')).grid(row=1,column=3)
        self.brace1 = Button(self.root, text='(', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=lambda: self.get_num('(')).grid(row=1, column=4)
        self.sin=Button(self.root,text='sin',bd=8,font=16,bg='dark gray',fg='black',width=4,height=2,command=lambda:self.get_num('sin(')).grid(row=1,column=5)
        self.btn4 = Button(self.root, text='4',bd=8, font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('4')).grid(row=2, column=0)
        self.btn5 = Button(self.root, text='5',bd=8,font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('5')).grid(row=2, column=1)
        self.btn6 = Button(self.root, text='6', bd=8,font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('6')).grid(row=2, column=2)
        self.btnsub = Button(self.root, text='-',bd=8,font=16, bg='dark gray',fg='black', width=4, height=2,command=lambda:self.get_num('-')).grid(row=2, column=3)
        self.brace2 = Button(self.root, text=')', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=lambda: self.get_num(')')).grid(row=2, column=4)
        self.cos = Button(self.root, text='cos', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=lambda: self.get_num('cos(')).grid(row=2, column=5)
        self.btn7 = Button(self.root, text='7', bd=8,font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('7')).grid(row=3, column=0)
        self.btn8 = Button(self.root, text='8',bd=8,font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('8')).grid(row=3, column=1)
        self.btn9 = Button(self.root, text='9',bd=8,font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('9')).grid(row=3, column=2)
        self.btndiv = Button(self.root, text='/',bd=8,font=16, bg='dark gray',fg='black', width=4, height=2,command=lambda:self.get_num('/')).grid(row=3, column=3)
        self.log = Button(self.root, text='log', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=lambda: self.get_num('log(')).grid(row=3, column=4)
        self.btnclr = Button(self.root, text='CLR', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=self.clr).grid(row=4, column=4)
        self.tan = Button(self.root, text='tan', bd=8, font=16, bg='dark gray', fg='black', width=4, height=2,command=lambda: self.get_num('tan(')).grid(row=3, column=5)
        self.dec = Button(self.root,text='.', bd=8,font=16, bg='dark gray',fg='black', width=4, height=2,command=lambda:self.get_num('.')).grid(row=4, column=0)
        self.btn0 = Button(self.root, text='0',bd=8, font=16,bg='gray',fg='White',width=4,height=2,command=lambda:self.get_num('0')).grid(row=4, column=1)
        self.btneql = Button(self.root, text='=',bd=8,font=16, bg='dark gray',fg='black', width=4, height=2,command=self.get_result).grid(row=4, column=2)
        self.btnmul = Button(self.root, text='*',bd=8,font=16, bg='dark gray',fg='black', width=4, height=2,command=lambda:self.get_num('*')).grid(row=4, column=3)
        self.btnac = Button(self.root, text='AC', bd=8, font=16, bg='maroon', fg='white', width=4, height=2,command=self.clear).grid(row=4, column=5)

        self.root.mainloop()

    def get_num(self,num):
        if self.operator=="Undefined!" or self.operator=="Syntax Error!":
            self.text_var.set("")
            self.operator=""
        self.operator=self.operator+num
        self.text_var.set(self.operator)

    def clear(self):
        self.operator=""
        self.text_var.set(self.operator)

    def clr(self):
        if self.operator=="Undefined!" or self.operator=="Syntax Error!":
            self.text_var.set("")
            self.operator=""
        else:
            txt=self.operator
            self.operator = txt[0:len(txt)-1]
            self.text_var.set(self.operator)

    def get_result(self):
        txt = self.operator
        self.text_var.set("")
        try:
            txt=str(eval(txt))
        except ZeroDivisionError:
            self.operator='Undefined!'
            self.text_var.set(self.operator)
        except SyntaxError:
            self.operator="Syntax Error!"
            self.text_var.set(self.operator)
        except NameError:
            self.operator = "Syntax Error!"
            self.text_var.set(self.operator)
        else:
            self.operator=txt
            self.text_var.set(self.operator)

obj1=calculator()
