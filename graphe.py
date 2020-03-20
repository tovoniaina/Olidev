from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolBar
from matplotlib.figure import Figure
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
#import index import *

class Fenetre(QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.setWindowTitle("APPLICATION OLIDEV")
        self.resize(500,500)
        self.setWindowIcon(QIcon("ONLINE.ICO"))
        self.centralWidget=QWidget()
        self.setCentralWidget(self.centralWidget)


        #Creation champs ID et Nom
        self.label1=QLabel("ID: ",self.centralWidget)
        self.text1=QLineEdit(self.centralWidget)

        self.label2=QLabel("Nom: ",self.centralWidget)
        self.text2=QLineEdit(self.centralWidget)



        qhboxlayout=QHBoxLayout()
        qhboxlayout2=QHBoxLayout()

        qhboxlayout.addWidget(self.label1)
        qhboxlayout.addWidget(self.text1)

        qhboxlayout2.addWidget(self.label2)
        qhboxlayout2.addWidget(self.text2)



        #Ajout bouton
        self.boutton1=QPushButton("Add",self.centralWidget)

        self.on_click()
        qvboxlayout=QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)
        qvboxlayout.addLayout(qhboxlayout2)


        qvboxlayout.addWidget(self.boutton1)
        #Creation evenement
        self.boutton1.clicked.connect(self.on_click)

    def on_click(self):
        valeur1=self.text1.text()
        valeur2=self.text2.text()
        matuple=(valeur1,valeur2)


    def requete(self):
        xcon=sqlite3.connect("mabase.db")
        xcur=xcon.cursor()
        try:
            xcur.execute("create table if not exists user(id integer, nom string(25))")
            print("Table created")
        except:
            QMessageBox.about(self,"Info", "Error creating table")

        xcon.commit()
        xcon.close()
