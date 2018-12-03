import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar,
                             QFrame, QStackedLayout, QBoxLayout)
from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()


class App(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")

        self.create_app()
        self.setBaseSize(1366, 768)

    def create_app(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)

        # Create Tabs
        self.tab_bar = QTabBar(movable=True, tabsClosable=True)
        self.tab_bar.tabCloseRequested.connect(self.close_tab)

        self.tab_bar.setCurrentIndex(0)

        # Keep track of tabs
        self.tab_count = 0
        self.tabs = []

        # Create AddressBar
        self.tool_bar = QWidget()
        self.tool_bar_layout = QHBoxLayout()
        self.address_bar = AddressBar()

        self.tool_bar.setLayout(self.tool_bar_layout)
        self.tool_bar_layout.addWidget(self.address_bar)

        # New tab button
        self.add_tab_button = QPushButton("+")
        self.add_tab_button.clicked.connect(self.add_tab)

        self.tool_bar_layout.addWidget(self.add_tab_button)

        # Set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tab_bar)
        self.layout.addWidget(self.tool_bar)
        self.layout.addWidget(self.container)

        self.setLayout(self.layout)

        self.add_tab()

        self.show()

    def add_tab(self):
        i = self.tab_count

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab" + str(i))

        # Open web-view
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("https://google.com"))

        # Add web-view to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)

        # Set top level tab from [] to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        # Add tab to top level stacked widget
        self.container.layout.addWidget(self.tabs[i])
        self.container.layout.setCurrentWidget(self.tabs[i])

        # Set the tab at the top of the screen
        self.tab_bar.addTab("New Tab")
        self.tab_bar.setTabData(0,"tab")
        self.tab_bar.setCurrentIndex(i)

    def close_tab(self, i):
        self.tab_bar.removeTab(i)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())