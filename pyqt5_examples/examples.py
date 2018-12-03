from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import os
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # progress bar
        self.pbar = QProgressBar()
        self.pbar.setMaximumWidth(120)

        # creating home page
        self.browser = QWebEngineView(loadProgress=self.pbar.setValue, loadFinished=self.pbar.hide,
                                      loadStarted=self.pbar.show, titleChanged=self.setWindowTitle)
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        # creating statusbar
        self.browser.setMinimumSize(1200, 600)
        self.status = self.statusBar()
        self.status.addPermanentWidget(self.pbar)

        self.show()
        self.setWindowTitle("Cosmo")
        self.setWindowIcon(QIcon("cosmo.png"))
        # adding toolbar
        tb2 = QToolBar("Shortcuts")
        tb2.setIconSize(QSize(45, 45))
        self.addToolBar(Qt.RightToolBarArea, tb2)

        wiki_btn = QAction(QIcon("wiki.png"), "Wikipedia", self)
        wiki_btn.setStatusTip("Go to Wikipedia - The Free Encyclopedia")
        wiki_btn.triggered.connect(lambda: self.conn("http://www.wikipedia.com"))
        tb2.addAction(wiki_btn)

        fb_btn = QAction(QIcon("facebook.png"), "Facebook", self)
        fb_btn.setStatusTip("Go to Facebook")
        fb_btn.triggered.connect(lambda: self.conn("http://www.facebook.com"))
        tb2.addAction(fb_btn)

        y_btn = QAction(QIcon("yahoo.png"), "Yahoo!", self)
        y_btn.setStatusTip("Go to Yahoo")
        y_btn.triggered.connect(lambda: self.conn("http://www.yahoo.com"))
        tb2.addAction(y_btn)


app=QApplication(sys.argv)
window=MainWindow()
window.show()
sys.exit(app.exec())