
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
import sqlite3
#Creation de la classe pour Interface
class Fenetre1(QMainWindow):
    def __init__(self):
        super(Fenetre1, self).__init__()
        self.setWindowTitle("Gestion de Bibliotheque")
        self.resize(400,500)
        self.setWindowIcon(QIcon("book.ico"))
        self.setStyleSheet("QWidget{background:#e6ecff}")

        #creation responsive
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        #CCreation de text QlineEdit
        self.label1 =QLabel("ID",self.centralWidget)
        self.text1 = QLineEdit(self.centralWidget)
        self.text1.setPlaceholderText("Veuiller entrer lD de lecteur")

        self.label2 = QLabel("Nom ",self.centralWidget)
        self.text2 = QLineEdit(self.centralWidget)
        self.text2.setPlaceholderText("Veuiller entrer votre Nom")

        self.label3 = QLabel("Date ", self.centralWidget)
        self.text3 = QLineEdit(self.centralWidget)
        self.text3.setPlaceholderText("Veuiller entrer votre Ndate de naissance")

        # Tablewidget
        self.table1 = QTableWidget(self.centralWidget)
        self.table1.setRowCount(3)
        self.table1.setColumnCount(3)
        #definir la colonne
        self.table1.setHorizontalHeaderLabels(['ID', 'NOM','DATE'])

        #bouton
        self.btn1 = QPushButton("SUBMIT",self.centralWidget)
        #style css bouton




        #Layout
        qhboxlayout = QHBoxLayout()
        qhboxlayout2 = QHBoxLayout()
        qhboxlayout3 = QHBoxLayout()

        qhboxlayout.addWidget(self.label1)
        qhboxlayout.addWidget(self.text1)

        qhboxlayout2.addWidget(self.label2)
        qhboxlayout2.addWidget(self.text2)

        qhboxlayout3.addWidget(self.label3)
        qhboxlayout3.addWidget(self.text3)




        qvboxlayout = QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)
        qvboxlayout.addLayout(qhboxlayout2)
        qvboxlayout.addLayout(qhboxlayout3)

        qvboxlayout.addWidget(self.table1)
        qvboxlayout.addWidget(self.btn1)
        # appel Click
        self.btn1.clicked.connect(self.click)
        #Appel affichage tableau
        self.requete_affichage()

    #fonction click
    def click(self):
        val1 =self.text1.text()
        val2 = self.text2.text()
        val3 = self.text3.text()
        #val1 = 8
        #val2 ='Jesica'
        #val3 ='08/02/90'

        matuple =(val1,val2,val3)
        if val1 =="" or val2 =="" or val3 =="":
            QMessageBox.about(self,"info","Champ de texte vide")
        else:
            self.requete(matuple)
            self.requete_affichage()
        #self.requete()


    #requete a la base de donner
    def requete(self,xtuple):
        con = sqlite3.connect("testa.db")
        cur = con.cursor()
        print("connection a Bdd ok")
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS lecteur(id integer  PRIMARY KEY,nom string(25),date_naissance date)")
        except:
            QMessageBox.about(self,"info","erreur creation table")
        try:
            cur.execute("INSERT INTO lecteur (ID,nom,date_naissance) VALUES(?,?,?)",xtuple)
            print("Insertion a la database testb ok")
        except:
            QMessageBox.about(self,"Information","erreur insertion")

        con.commit()
        con.close()
    #requete affichage
    def requete_affichage(self):
        con = sqlite3.connect("testa.db")
        res = con.execute("select * from lecteur")
        self.table1.setRowCount(0)
        for y1, y2 in enumerate(res):
            self.table1.insertRow(y1)
            for x1, x2 in enumerate(y2):
                self.table1.setItem(y1, x1, QTableWidgetItem(str(x2)))
        con.close()



