from tkinter import *
import urllib.request
import webbrowser
from tkinter.colorchooser import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

class Browser:
    def __init__(self):
        self.root=Tk()
        self.root.title("Fast Browse")

        menu = Menu(self.root)
        self.root.config(menu=menu)

        subMenu = Menu(menu)
        menu.add_cascade(label="Apps", menu=subMenu)
        subMenu.add_command(label="Gmail")
        subMenu.add_command(label="Y! Mail")
        subMenu.add_command(label="Youtube")
        subMenu.add_command(label="Facebook")
        subMenu.add_command(label="Github")
        subMenu.add_command(label="LinkedIn")
        subMenu.add_separator()
        editMenu = Menu(menu)
        menu.add_cascade(label="Settings", menu=editMenu)
        editMenu.add_command(label="Themes and Colors", command=self.getColor)
        editMenu.add_command(label="History")
        editMenu.add_command(label="Connect account...")
        editMenu.add_command(label="Exit", command=self.root.quit)
        editMenu = Menu(menu)
        menu.add_cascade(label="Bookmarks", menu=editMenu)
        editMenu.add_command(label="View")
        editMenu.add_command(label="Add bookmark")
        editMenu = Menu(menu)
        menu.add_cascade(label="Tools", menu=editMenu)
        editMenu.add_command(label="Inspect Element")
        editMenu.add_command(label="Manage Extensions")
        editMenu.add_command(label="Developer Tools")
        editMenu = Menu(menu)
        menu.add_cascade(label="Downloads", menu=editMenu)
        editMenu.add_command(label="Open Downloads Folder", command=self.callback)

        Label(self.root, text='Enter URL', font=("Helvetica", 14)).pack(side=TOP)

        self.e1 = Entry(self.root, width=100)
        self.e1.pack(side=TOP)

        Button(self.root, text='Go', width=10, relief=RAISED, font=("Helvetica", 12), command=self.url).pack(side=TOP)

        Label(self.root, text='Quick Links : ', font=("Helvetica", 16)).pack(side=BOTTOM)

        # This binds the return key to self.browse as an alternative to clicking the button.
        self.root.bind_all('<Enter>', self.url)
        self.root.mainloop()

    def url(self):
        webbrowser.open_new(self.e1.get())

    def getColor(self):
        pass

    def callback(self):
        pass

    def browse(self):
        pass

obj1=Browser()