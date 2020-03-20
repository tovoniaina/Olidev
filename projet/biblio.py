#Projet de Gedtion de Bibliotheque versus Lecteur
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from lecteur import *
import pymysql

#Creation de la classe pour Interface
class Fenetre(QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.setWindowTitle("Gestion de Bibliotheque")
        self.resize(400,500)
        self.setWindowIcon(QIcon("boky.ico"))
        self.setStyleSheet("QWidget{background:#e6ecff}")

        #creation responsive
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #CCreation de Bouton QPushboyuton
        self.btn1 = QPushButton("Ajout Lecteur",self.centralWidget)
        self.btn2 = QPushButton("Ajout Livre",self.centralWidget)
        self.btn3 = QPushButton("Traitement", self.centralWidget)
        #style css bouton

        self.btn1.setStyleSheet("QWidget{background:#00cccc;}")
        self.btn2.setStyleSheet("QWidget{background:#00cccc;}")
        self.btn3.setStyleSheet("QWidget{background:#99b3ff;}")


        #Layout
        qhboxlayout = QHBoxLayout()
        qvboxlayout = QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)

        #add centralwidget
        qvboxlayout.addWidget(self.btn1)
        qvboxlayout.addWidget(self.btn2)
        qvboxlayout.addWidget(self.btn3)


        #appele le click
        #self.btn1.clicked.connect(self.requete)

    #fonction click
    def click(self):
        centralWidget = QWidget()
        layout = QVBoxLayout()
        # Table Widget
        self.tableWidget = QTableWidget()
        # ligne
        self.tableWidget.setRowCount(3)
        # colonne
        self.tableWidget.setColumnCount(3)
        # Mandoko
        self.tableWidget.setStyleSheet("QWidget{background:cyan}")
        # Miantso CentralWidget
        centralWidget.setLayout(layout)
        self.setCentralWidget(centralWidget)
        # label
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Nom', 'Adresse'])
        # affichet table
        layout.addWidget(self.tableWidget)
        #miantso requete

    def requete(self):

        con = sqlite3.connect("testa.db")
        res = con.execute("SELECT * FROM lecteur")
        #cur.execute("SELECT * FROM lecteur")
        #res = cur.fetchall()
        #for x in res:
            #print(x)
        #boucle pour affiuchage
        self.tableWidget.setRowCount(0)
        self.table1.setRowCount(0)
        for y1, y2 in enumerate(res):
            self.table1.insertRow(y1)
            for x1, x2 in enumerate(y2):
                self.table1.setItem(y1, x1, QTableWidgetItem(str(x2)))
        con.close()


#Affichage de l'interface
app= QApplication.instance()

if not app:
    app = QApplication(sys.argv)

#Lancement de fonction/Classe
fenetre = Fenetre()
fenetre.show()
app.exec_()
