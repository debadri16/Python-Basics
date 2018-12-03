
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import*
from PyQt5.QtWebEngine import *
from PyQt5.QtWebEngineCore import *
from PyQt5.QtWebSockets import *
import PyQt5

import sys

class MainWin(MainWin):
    def __init__(self,*args,**kwargs):
        super(MainWin,self).__init__(*args,**kwargs)

        self.setWindowTitle("abcd")
        self.browser=QWebView()
        self.browser.setUrl(QUrl("www.google.com"))
        self.setCentralWidget(self.browser)

app=QApplication(sys.argv)
window=MainWin()
window.show()
app.exec_()