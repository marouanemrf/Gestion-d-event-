from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_erreur(object):
    def setupUi(self, erreur):
        erreur.setObjectName("erreur")
        erreur.resize(495, 300)
        erreur.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        erreur.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(erreur)
        self.widget.setGeometry(QtCore.QRect(30, 40, 441, 191))
        self.widget.setStyleSheet("background-color: rgb(255, 64, 64);\n"
"border-radius: 5px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 30, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 120, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 183, 147);\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 60, 34);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(erreur)
        QtCore.QMetaObject.connectSlotsByName(erreur)

    def retranslateUi(self, erreur):
        _translate = QtCore.QCoreApplication.translate
        erreur.setWindowTitle(_translate("erreur", "Form"))
        self.label.setText(_translate("erreur", "Votre mots de pass ou le nom est incorrecte ou le visage est inconnue!!!"))
        self.pushButton_2.setText(_translate("erreur", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    erreur = QtWidgets.QWidget()
    ui = Ui_erreur()
    ui.setupUi(erreur)
    erreur.show()
    sys.exit(app.exec_())
