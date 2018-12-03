from tkinter import *
import tkinter.scrolledtext as Text1
from tkinter.filedialog import *
from tkinter.messagebox import *
class notepad:

    def __init__(self):

        #DRIVER FUNCTION
        self.root=Tk()
        self.root.title("pytext")
        self.root.maxsize(width=1000,height=1000)
        self.root.minsize(width=400,height=400)
        self.fontstyle="normal"
        self.font="Courier New"
        self.fontsize=12
        self.text=Text1.ScrolledText(self.root,relief="sunken",bd=2,width=400,height=400)
        self.text.pack()
        self.firstsave=0


        # MENU BAR
        menu = Menu(self.root)
        self.root.config(menu=menu)

        filemenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="New...", command=self.newFile, accelerator="Ctrl+N")
        filemenu.add_command(label="Open...", command=self.openFile,accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=self.saveFile,accelerator="Ctrl+S")
        filemenu.add_command(label="SaveAs..", command=self.saveAs,accelerator="Ctrl+Shift+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit,accelerator="Alt+F4")

        editmenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="Edit", menu=editmenu)

        editmenu.add_command(label="Cut", command=self.Cut,accelerator="Ctrl+X")
        editmenu.add_command(label="Copy", command=self.Copy,accelerator="Ctrl+C")

        editmenu.add_command(label="Paste", command=self.Paste,accelerator="Ctrl+V")

        formatmenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="Format", menu=formatmenu)

        formatmenu.add_command(label="Font", command=self.Font)
        formatmenu.add_command(label="Font Size", command=self.Fontsize)
        formatmenu.add_command(label="Font Style", command=self.Fontstyle)

        aboutmenu = Menu(menu,tearoff=0)
        menu.add_cascade(label="About", menu=aboutmenu)
        aboutmenu.add_command(label="Info.", command=self.info)

        #keyboard shortcuts
        self.root.bind("<Control-N>",self.newFile)
        self.root.bind("<Control-O>",self.openFile)
        self.root.bind("<Control-S>",self.saveFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-Shift-S>",self.saveAs)
        self.root.bind("<Control-X>",self.Cut)
        self.root.bind("<Control-C>",self.Copy)
        self.root.bind("<Control-V>",self.Paste)
        self.root.bind("<Alt-F4>",self.Exit)

        self.fontvar = StringVar()  # variable for radiobutton.
        self.fontvar.set(self.font)
        self.style = StringVar()  # style variable for radiobutton
        self.style.set(self.fontstyle)
        # Set the font, font size and font style:
        self.text.config(font=(self.font, self.fontsize, self.fontstyle,))

        self.root.mainloop()

    #filemenu functions
    def newFile(self,event=NONE):
        if self.firstsave==0:
            self.newsave()
        else:
            self.filename = "Untitled"
            self.text.delete(0.0, END)
            self.firstsave=0

    def openFile(self,event=NONE):
        f=askopenfile(mode='r', filetypes=[("text file", "*.txt")])
        self.filename=f.name
        t=f.read()
        self.text.delete(0.0,END)
        self.text.insert(0.0,t)
        self.firstsave=1

    def saveFile(self,event=NONE):
        if self.firstsave==0:
            f = asksaveasfile(title="Save",defaultextension=".txt", filetypes=[("text file", "*.txt")])
            t = self.text.get(0.0, END)
            try:
                f.write(t.rstrip())
            except:
                showerror(title="Opps!", message="Unable to save file!")
        else:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
            self.firstsave = 1

    def saveAs(self,event=NONE):
        f = asksaveasfile(title="SaveAs",defaultextension=".txt", filetypes=[("text file", "*.txt")])
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Opps!", message="Unable to save file!")
        self.firstsave = 1


    def newsave(self):
        f = asksaveasfile(title="Save current file!",defaultextension=".txt", filetypes=[("text file", "*.txt")])
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Opps!", message="Unable to save file!")
        self.firstsave = 1
        self.newFile()

    def Exit(self,event=NONE):
        if self.firstsave==0 and self.text.get(0.0,END)!="\n":
            userinput=askquestion("File not saved.","Do you want to save this file?")
            if userinput=='yes':
                self.saveAs()
        self.root.quit()

    #editmenu functions

    def Copy(self,event=NONE):
        self.root.clipboard_clear()
        self.text.clipboard_append(string=self.text.selection_get())

    def Cut(self,event=NONE):
        self.root.clipboard_clear()
        self.text.clipboard_append(string=self.text.selection_get())
        self.text.delete(index1=SEL_FIRST,index2=SEL_LAST)
    def Paste(self,event=NONE):
        self.text.insert(INSERT,self.root.clipboard_get())

    #format menu functions

    #font style--------------------------------------------------------------------
    def Fontstyle(self):
        self.top = Toplevel()
        self.top.title("Font Style")
        label = Label(self.top, text="Please select a font style...", width=30)
        label.pack()
        styles = (
                "normal",
                "bold",
                "italic")
        for style in styles:
            Radiobutton(self.top, text=style, value=style, variable=self.style).pack(anchor=W)

        frame = Frame(self.top)
        frame.pack()
        applyButton = Button(frame, text="Apply", command=self.applyfontstyle)
        applyButton.pack(side=LEFT)
        acceptButton = Button(frame, text="Accept", command=self.applyfontstyle_exit)
        acceptButton.pack(side=RIGHT)

    def applyfontstyle(self):
        self.fontstyle = self.style.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))

    def applyfontstyle_exit(self):
        self.fontstyle = self.style.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))
        self.top.destroy()


    # change font
    def Font(self):
        self.top = Toplevel()
        self.top.title("Font")

        label = Label(self.top, text="Please select a font...", width=30)
        label.pack()

        fonts = (
            "Arial",
            "Courier New",
            "Verdana",
            "Times New Roman",
            "Comic Sans MS",
            "Fixedsys",
            "MS Sans Serif",
            "MS Serif",
            "Symbol",
            "System")

        for font in fonts:
            Radiobutton(self.top, text=font, variable=self.fontvar, value=font).pack(anchor=W)

        frame = Frame(self.top)
        frame.pack()
        applyButton = Button(frame, text="Apply", command=self.applyfont)
        applyButton.pack(side=LEFT)
        acceptButton = Button(frame, text="Accept", command=self.applyfont_exit)
        acceptButton.pack(side=RIGHT)

    def applyfont(self):
        self.font = self.fontvar.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))

    def applyfont_exit(self):
        self.font = self.fontvar.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))
        self.top.destroy()

    #font size
    def Fontsize(self):
        self.top = Toplevel()
        self.top.title("Font Size")

        label = Label(self.top, text="Please select a font size...", width=30)
        label.pack()

        self.scale = Scale(self.top, from_=8, to=72, orient=HORIZONTAL)
        self.scale.pack()
        self.scale.set(self.fontsize)

        frame = Frame(self.top)
        frame.pack()
        applyButton = Button(frame, text="Apply", command=self.applyfontsize)
        applyButton.pack(side=LEFT)
        acceptButton = Button(frame, text="Accept", command=self.applyfontsize_exit)
        acceptButton.pack(side=RIGHT)

    def applyfontsize(self):
        self.fontsize = self.scale.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))

    def applyfontsize_exit(self):
        self.fontsize = self.scale.get()
        self.text.config(font=(self.font, self.fontsize, self.fontstyle))
        self.top.destroy()

    def info(self):
        showinfo("Information","This a text editor made using python :)")

nt=notepad()