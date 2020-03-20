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

class Poste(QMainWindow):
    def __init__(self):
        super(Poste, self).__init__()
        self.setWindowTitle("Ajout nouveau poste")
        self.resize(400,500)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        self.label1=QLabel("ID poste",self.centralWidget)
        self.text1=QLineEdit(self.centralWidget)

        self.label2=QLabel("Nom du poste",self.centralWidget)
        self.text2=QLineEdit(self.centralWidget)

        qhboxlayout=QHBoxLayout()
        qhboxlayout2=QHBoxLayout()

        qhboxlayout.addWidget(self.label1)
        qhboxlayout.addWidget(self.text1)

        qhboxlayout2.addWidget(self.label2)
        qhboxlayout2.addWidget(self.text2)

        #Bouton ajout nouveau poste
        self.btn1=QPushButton("Ajouter nouveau poste",self.centralWidget)
        #mise en forme bouton
        self.btn1.setStyleSheet("QWidget{background:green}")

        self.table1=QTableWidget(self.centralWidget)
        self.table1.setRowCount(2)
        self.table1.setColumnCount(2)


        qvboxlayout = QVBoxLayout(self.centralWidget)
        qvboxlayout.addLayout(qhboxlayout)
        qvboxlayout.addLayout(qhboxlayout2)

        qvboxlayout.addWidget(self.btn1)
        qvboxlayout.addWidget(self.table1)

        self.btn1.clicked.connect(self.on_click)
    def on_click(self):
        valeur1=self.text1.text()
        valeur2=self.text2.text()
        matuple=(valeur1,valeur2)
        if valeur1=="" or valeur2=="":
            QMessageBox.about(self,"info","Champs vide")
        else:
            self.connection(matuple)
            self.affichage()

    def connection(self,xtuple):
        xcon=sqlite3.connect("societe.db")
        xcur=xcon.cursor()

        try:
            xcur.execute("create table if not exists user(id integer, nom string(25))")
        except:
            QMessageBox.about(self,"info","Error creation table")

        try:
            xcur.execute("insert into user(id,nom) values(?,?)",xtuple)
            QMessageBox.about(self, "Info", "Succès")
        except:
            QMessageBox.about(self,"Info","Erreur")
        xcon.commit()
        xcon.close()

    def affichage(self):
        xcon=sqlite3.connect("societe.db")
        resultat=xcon.execute("select * from user")
        self.table1.setRowCount(0)
        for y1,y2 in enumerate(resultat):
            self.table1.insertRow(y1)
            for x1,x2 in enumerate(y2):
                self.table1.setItem(y1,x1,QTableWidgetItem(str(x2)))
        xcon.close()





app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
fenetre = Poste()
fenetre.show()
app.exec_()