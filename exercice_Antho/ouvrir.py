# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtGui, QtCore
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Fenetre(QMainWindow):

    def __init__(self):
        # Initialisation
        super(Fenetre, self).__init__()

        self.window = QWidget()
        self.window.setWindowTitle("Mon fenetre")
        self.window.resize(425, 370)

        self.centralWidget=QWidget()
        self.setCentralWidget(self.centralWidget)


        self.boutton1 = QPushButton("Nouvelle Fenetre", self.window)

        qhboxlayout=QHBoxLayout()
        qhboxlayout.addWidget(self.boutton1)

        qvboxlayout=QHBoxLayout(self.window)
        qvboxlayout.addLayout(qhboxlayout)

        self.boutton1.clicked.connect(self.test)
        self.window.show()

    def test(self):
        self.wind2xxxxx = Fenetre2()

class Fenetre2(QMainWindow):
    def __init__(self):
        super(Fenetre2, self).__init__()
        self.window = QWidget()
        self.window.setWindowTitle("Deuxième fenetre")
        self.window.resize(425, 370)
        self.window.show()


app=QApplication.instance()
if not app:
    app=QApplication(sys.argv)
fenetre=Fenetre()
app.exec_()