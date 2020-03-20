#from index import *
from graphe import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
fenetre = Fenetre()
fenetre.show()
app.exec_()
