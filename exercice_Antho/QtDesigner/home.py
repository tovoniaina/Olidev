# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ApplicationGestionPersonnel(object):
    def setupUi(self, ApplicationGestionPersonnel):
        ApplicationGestionPersonnel.setObjectName("ApplicationGestionPersonnel")
        ApplicationGestionPersonnel.resize(370, 428)
        self.centralwidget = QtWidgets.QWidget(ApplicationGestionPersonnel)
        self.centralwidget.setWindowTitle("Application Gestion Personnel")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 210, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 351, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 270, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 330, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        ApplicationGestionPersonnel.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ApplicationGestionPersonnel)
        self.statusbar.setObjectName("statusbar")
        ApplicationGestionPersonnel.setStatusBar(self.statusbar)

        self.retranslateUi(ApplicationGestionPersonnel)
        QtCore.QMetaObject.connectSlotsByName(ApplicationGestionPersonnel)

    def retranslateUi(self, ApplicationGestionPersonnel):
        _translate = QtCore.QCoreApplication.translate
        ApplicationGestionPersonnel.setWindowTitle(_translate("ApplicationGestionPersonnel", "MainWindow"))
        self.pushButton.setText(_translate("ApplicationGestionPersonnel", "Ajouter nouveau poste"))
        self.textBrowser.setHtml(_translate("ApplicationGestionPersonnel", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">Bienvenue,</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ce logiciel vous permet de faire ces actions suivantes:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">- Ajouter nouveau poste disponible dans une société</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">- Ajouter nouveau collaborateur</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">- Traitement de leurs informations</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Merci et bon usage</span></p></body></html>"))
        self.pushButton_2.setText(_translate("ApplicationGestionPersonnel", "Ajouter nouveau employé"))
        self.pushButton_3.setText(_translate("ApplicationGestionPersonnel", "Traitement des données"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ApplicationGestionPersonnel = QtWidgets.QMainWindow()
    ui = Ui_ApplicationGestionPersonnel()
    ui.setupUi(ApplicationGestionPersonnel)
    ApplicationGestionPersonnel.show()
    sys.exit(app.exec_())
