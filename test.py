import sys
from PyQt5 import QtCore, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import get_test_data


class Fenetre1(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Entrer les données")
        self.resize(700,800)
        layout = QtWidgets.QGridLayout()


        self.label1=QtWidgets.QLabel("ID Poste") #Libéllé ID
        self.line_edit1 = QtWidgets.QLineEdit() #Champs que nous allons entrer l'ID
        layout.addWidget(self.label1)
        layout.addWidget(self.line_edit1)

        self.label2 = QtWidgets.QLabel("Nom du Poste")  # Libéllé ID
        self.line_edit2 = QtWidgets.QLineEdit()  # Champs que nous allons entrer l'ID
        layout.addWidget(self.label2)
        layout.addWidget(self.line_edit2)

        #Ici l'interface qu'on permet entrer nos données dans le DB (dans mon cas ici, on entre ID poste & Nom poste)
        self.button = QtWidgets.QPushButton('Entrer les Données')
        self.button.clicked.connect(self.switch) #Emettre les données
        layout.addWidget(self.button)
        self.setLayout(layout)

        #Ce bouton nous permet de sortir du programme
        self.button = QtWidgets.QPushButton('Sortir du programme')
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)
        self.setLayout(layout)

        #Ici on crée un table permettant d'afficher les données que nous allons entrer dans le formulaire ci-dessous
        self.table = QTableWidget(self)
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID Poste', 'Nom du Poste'])
        layout.addWidget(self.table)
        self.affichage()

    def switch(self):
        #self.switch_window.emit(self.line_edit1.text())
        #self.switch_window.emit(self.line_edit2.text())
        valeur1 = self.line_edit1.text()
        valeur2 = self.line_edit2.text()
        matuple = (valeur1, valeur2)
        if valeur1 == "" or valeur2 == "":
            QMessageBox.about(self,"info","Champs vide, veuillez les remplir")
        else:
            self.connection(matuple)
            self.affichage()

    #C'est à partir de cette fonction qu'on peut ajouter des nouvelles données dans la table de notre DB SQLite
    def connection(self,xtuple):
        xcon = sqlite3.connect("societe.db")
        xcur = xcon.cursor()

        try:
            xcur.execute("create table if not exists user(id integer, nom string(25))")
        except:
            QMessageBox.about(self,"info","Error creation Table")

        try:
            xcur.execute("insert into user(id,nom) values(?,?)",xtuple)
            QMessageBox.about(self, "info","Succès")
        except:
            QMessageBox.about(self, "info","Error")
        xcon.commit()
        xcon.close()

    #Ici, on va afficher dans un tableau les données qu'on a dans la table de notre DB SQLite :)
    def affichage(self):
        xcon = sqlite3.connect("societe.db")
        resultat = xcon.execute("select * from user")
        self.table.setRowCount(0)
        for y1, y2 in enumerate(resultat):
            self.table.insertRow(y1)
            for x1, x2 in enumerate(y2):
                self.table.setItem(y1, x1, QTableWidgetItem(str(x2)))
        xcon.close()


class Fenetre2(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Entrer les données nouveau employé")
        self.resize(700,800)
        layout = QtWidgets.QGridLayout()


        self.label1=QtWidgets.QLabel("IM Employé") #IM Employé
        self.line_edit1 = QtWidgets.QLineEdit() #Champs que nous allons entrer l'ID
        layout.addWidget(self.label1)
        layout.addWidget(self.line_edit1)

        self.label2 = QtWidgets.QLabel("Nom Complet de l'employé")  # Libéllé ID
        self.line_edit2 = QtWidgets.QLineEdit()  # Champs que nous allons entrer l'ID
        layout.addWidget(self.label2)
        layout.addWidget(self.line_edit2)

        #Ici l'interface qu'on permet entrer nos données dans le DB (dans mon cas ici, on entre IM Employé & Nom Complet de l'employé)
        self.button = QtWidgets.QPushButton('Entrer les Données')
        self.button.clicked.connect(self.switch) #Emettre les données
        layout.addWidget(self.button)
        self.setLayout(layout)

        #Ce bouton nous permet de sortir du programme
        self.button = QtWidgets.QPushButton('Sortir du programme')
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)
        self.setLayout(layout)

        #Ici on crée un table permettant d'afficher les données que nous allons entrer dans le formulaire ci-dessous
        self.table = QTableWidget(self)
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["IM Employé", "Nom Complet de l'employé"])
        layout.addWidget(self.table)
        self.affichage()

    def switch(self):
        #self.switch_window.emit(self.line_edit1.text())
        #self.switch_window.emit(self.line_edit2.text())
        valeur1 = self.line_edit1.text()
        valeur2 = self.line_edit2.text()
        matuple = (valeur1, valeur2)
        if valeur1 == "" or valeur2 == "":
            QMessageBox.about(self,"info","Champs vide, veuillez les remplir")
        else:
            self.connection(matuple)
            self.affichage()

    #C'est à partir de cette fonction qu'on peut ajouter des nouvelles données dans la table de notre DB SQLite
    def connection(self,xtuple):
        xcon = sqlite3.connect("societe.db")
        xcur = xcon.cursor()

        try:
            xcur.execute("create table if not exists employe(id integer, nom string(25))")
        except:
            QMessageBox.about(self,"info","Error creation Table")

        try:
            xcur.execute("insert into employe(id,nom) values(?,?)",xtuple)
            QMessageBox.about(self, "info","Succès")
        except:
            QMessageBox.about(self, "info","Error")
        xcon.commit()
        xcon.close()

    #Ici, on va afficher dans un tableau les données qu'on a dans la table de notre DB SQLite :)
    def affichage(self):
        xcon = sqlite3.connect("societe.db")
        resultat = xcon.execute("select * from employe")
        self.table.setRowCount(0)
        for y1, y2 in enumerate(resultat):
            self.table.insertRow(y1)
            for x1, x2 in enumerate(y2):
                self.table.setItem(y1, x1, QTableWidgetItem(str(x2)))
        xcon.close()

class home(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Home')
        self.resize(250,250)
        layout = QtWidgets.QGridLayout()

        #La liste des boutons dans la fenetre Home
        self.button1 = QtWidgets.QPushButton('Ajouter un nouveau poste')
        self.button2 = QtWidgets.QPushButton('Ajouter nouvel employé')
        self.button3 = QtWidgets.QPushButton('Traitement des données')
        self.button4 = QtWidgets.QPushButton('Afficher les stats')

        #Mise en forme de boutons
        self.button1.setStyleSheet("QWidget{background:cyan}")
        self.button2.setStyleSheet("QWidget{background:orange}")
        self.button3.setStyleSheet("QWidget{background:pink}")
        self.button4.setStyleSheet("QWidget{background:blue}")

        #Faire intéragir le bouton
        self.button1.clicked.connect(self.home)
        self.button2.clicked.connect(self.home)
        self.button3.clicked.connect(self.home)
        self.button4.clicked.connect(self.home)

        #Adapter la visibilité des boutons à travers de la fenetre
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def home(self):
        self.switch_window.emit()


class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.home = home()
        self.home.switch_window.connect(self.show_main)
        self.home.show()

    def show_main(self):
        self.window = Fenetre1()
        self.window.switch_window.connect(self.show_window_two)
        self.home.close()
        self.window.show()

    def second_fenetre(self):
        self.window = Fenetre2()
        self.window.switch_window.connect(self.show_window_two)
        self.home.close()
        self.window.show()

    def show_window_two(self, text):
        self.window_two = WindowTwo(text)
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    controller.second_fenetre()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()