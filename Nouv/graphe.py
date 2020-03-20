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
from index import *
class Fenetre(QMainWindow):
    def __init__(self):
        super(Fenetre, self).__init__()
        self.setWindowTitle("OLIDEV APPLICATION")
        self.resize(500,600)
        self.setWindowIcon(QIcon("ONLINE.ICO"))
        self.centralWidget=QWidget()
        self.setCentralWidget(self.centralWidget)
        self.lancement_plot()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)

        self.label1=QLabel("ID: ",self.centralWidget)
        self.text1=QLineEdit(self.centralWidget)

        self.label2 = QLabel("Nom: ", self.centralWidget)
        self.text2 = QLineEdit(self.centralWidget)

        qhboxlayout=QHBoxLayout()
        qhboxlayout2 = QHBoxLayout()

        qhboxlayout.addWidget(self.label1)
        qhboxlayout.addWidget(self.text1)

        qhboxlayout2.addWidget(self.label2)
        qhboxlayout2.addWidget(self.text2)

        self.boutton1=QPushButton("Ampidirina",self.centralWidget)

        self.boutton2=QPushButton("Asaina avokoa ny ao anaty base",self.centralWidget)


        self.boutton1.setStyleSheet("QWidget{background:green}")
        self.boutton2.setStyleSheet("QWidget{background:red}")

        self.table1=QTableWidget(self.centralWidget)
        self.table1.setRowCount(2)
        self.table1.setColumnCount(2)
        self.table1.setStyleSheet("QWidget{background:white;"
                                  "margin-top:50px;"
                                  "}")

        qvboxlayout=QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)
        qvboxlayout.addLayout(qhboxlayout2)

        qvboxlayout.addWidget(self.boutton1)
        qvboxlayout.addWidget(self.boutton2)
        qvboxlayout.addWidget(self.table1)
        qvboxlayout.addWidget(self.canvas)
        qvboxlayout.addWidget(self.toolbar)
        #Evenement
        self.boutton1.clicked.connect(self.on_click)
        self.boutton2.clicked.connect(compar)
        #self.boutton1.clicked.connect(compar)
        self.requete_affichage()

    def on_click(self):
        valeur1=self.text1.text()
        valeur2=self.text2.text()
        matuple=(valeur1,valeur2)
        if valeur1=="" or valeur2=="":
            QMessageBox.about(self,"information","Champ texte vide")
        else:
            self.requete(matuple)
            self.requete_affichage()

    def requete(self,xtuple):
        xcon=sqlite3.connect("majessy.db")
        xcur=xcon.cursor()
        try:
            xcur.execute("create table if not exists user(id integer,nom string(25))")
        except:
            QMessageBox.about(self,"Info","Misy erreur ny creation base")
        try:
            xcur.execute("insert into user(id,nom) values(?,?)",xtuple)
        except:
            QMessageBox.about(self, "Info", "Misy erreur ny insertion")
        xcon.commit()
        xcon.close()

    def requete_affichage(self):
        xcon=sqlite3.connect("majessy.db")
        resultat=xcon.execute("select * from user")
        self.table1.setRowCount(0)
        for y1,y2 in enumerate(resultat):
            self.table1.insertRow(y1)
            for x1,x2 in enumerate(y2):
                self.table1.setItem(y1,x1,QTableWidgetItem(str(x2)))
        xcon.close()

    def lancement_plot(self):
        self.canvas=Graphe(self)
        self.show()

class Graphe(FigureCanvas):
    def __init__(self,parent=None):
        self.fig=Figure()
        self.plt=self.fig.subplots()
        self.fig=plt.Figure()

        FigureCanvas.__init__(self,self.fig)

        self.setParent(parent)
        # ERREUR FATAL self.canvas = FigureCanvas(self.fig)
        #self.toolbar=NavigationToolbar(self,self)
        self.requeteGraphe()

    def requeteGraphe(self):
        nb_formation=[]
        nb_formateur=[]
        with sqlite3.connect("majessy.db") as xcon:
            xcur=xcon.cursor()
            xcur.execute("select id, count(*) from user group by(id)")
            for formateur,formation in xcur.fetchall():
                nb_formateur.append(formateur)
                nb_formation.append(formation)
        self.plt = self.fig.add_subplot(111, projection='3d')
        x = nb_formateur
        y = nb_formation

        # self.plt.plot(x, y, '-r')
        # self.plt.plot(x, y, ':g')

        #self.plt.plot(x, y, '-r', label='Nombre d enregistrement', linewidth=5)
        self.plt.plot(x, y, label="Isan'ireo andraikitra sahanina", alpha=0.8,
                      color='RoyalBlue', linestyle='dotted', linewidth=3,
                      marker='o', markersize=8, markerfacecolor='SpringGreen',
                      markeredgecolor='blue')
        #self.plt.xlabel('ID utilisateur')

        #self.plt.plot(x, y, 'g', label='Nombre d enregistrement', linewidth=5)
        #self.plt.xlabel('ID utilisateur')
        self.plt.legend()

