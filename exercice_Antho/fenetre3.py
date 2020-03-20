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
        self.setWindowTitle("Affichage Stats")
        self.resize(700,700)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.lancement_plot()
        self.toolbar = NavigationToolbar(self.canvas, self.canvas)


    def lancement_plot(self):
        self.canvas = Graphe(self)
        self.show()

class Graphe(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = Figure()
        self.plt = self.fig.subplots()
        self.fig = plt.Figure()

        FigureCanvas.__init__(self, self.fig)

        self.setParent(parent)
        self.requeteGraphe()

    def requeteGraphe(self):
        nb_poste = []
        nb_employe = []
        with sqlite3.connect("societe.db") as xcon:
            xcur = xcon.cursor()
            xcur.execute("select id, count(*) from user group by(id)")
            for poste, employe in xcur.fetchall():
                nb_poste.append(poste)
                nb_employe.append(employe)
        self.plt = self.fig.add_subplot(111, projection='2d')
        x = nb_poste
        y = nb_employe

        self.plt.plot(x, y, label="Nb de poste", alpha=0.8,
                      color='RoyalBlue', linestyle='dotted', linewidth=3,
                      marker='o', markersize=8, markerfacecolor='SpringGreen',
                      markeredgecolor='blue')

        self.plt.legend()

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
fenetre = Poste()
fenetre.show()
app.exec_()