from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_quitter(object):
    def setupUi(self, quitter):
        quitter.setObjectName("quitter")
        quitter.resize(400, 300)
        quitter.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        quitter.setAttribute(QtCore.Qt.WA_TranslucentBackground)  
        self.qitter = QtWidgets.QWidget(quitter)
        self.qitter.setGeometry(QtCore.QRect(30, 50, 351, 151))
        self.qitter.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.483, radius:2, fx:0.568182, fy:0.585, stop:0.352273 rgba(253, 255, 244, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border-radius: 10px;")
        self.qitter.setObjectName("qitter")
        self.question = QtWidgets.QLabel(self.qitter)
        self.question.setGeometry(QtCore.QRect(70, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.question.setFont(font)
        self.question.setStyleSheet("\n"
"   color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) ); background-color: none;"
"")
        self.question.setObjectName("question")
        self.non = QtWidgets.QPushButton(self.qitter)
        self.non.setGeometry(QtCore.QRect(10, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.non.setFont(font)
        self.non.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.non.setObjectName("non")
        self.oui = QtWidgets.QPushButton(self.qitter)
        self.oui.setGeometry(QtCore.QRect(190, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.oui.setFont(font)
        self.oui.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.oui.setObjectName("oui")

        self.retranslateUi(quitter)
        QtCore.QMetaObject.connectSlotsByName(quitter)

        self.oui.clicked.connect(self.logout)

    def retranslateUi(self, quitter):
        _translate = QtCore.QCoreApplication.translate
        quitter.setWindowTitle(_translate("quitter", "Form"))
        self.question.setText(_translate("quitter", "Vous voulez vraiment quitter ??"))
        self.non.setText(_translate("quitter", "NON"))
        self.oui.setText(_translate("quitter", "OUI"))

    def logout(self):
        from login import Ui_loginForm 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_loginForm()

        self.work.setupUi(self.work_window)
        self.work_window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    quitter = QtWidgets.QWidget()
    ui = Ui_quitter()
    ui.setupUi(quitter)
    quitter.show()
    sys.exit(app.exec_())
