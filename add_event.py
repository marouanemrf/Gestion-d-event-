from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection

class Ui_ajouterevent(object):
    def setupUi(self, ajouterevent):
        ajouterevent.setObjectName("ajouterevent")
        ajouterevent.resize(526, 607)
        ajouterevent.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        ajouterevent.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.addevent = QtWidgets.QWidget(ajouterevent)
        self.addevent.setGeometry(QtCore.QRect(20, 20, 491, 471))
        self.addevent.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 #FF6961 );\n"
"    border-radius: 10px;\n"
"")
        self.addevent.setObjectName("addevent")
        self.close = QtWidgets.QPushButton(self.addevent)
        self.close.setGeometry(QtCore.QRect(470, 10, 12, 12))
        self.close.setStyleSheet("QPushButton{\n"
"    background-color: rgb(170, 0, 0);\n"
"    border-radius: 6px;\n"
"   border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(255, 0, 0);\n"
" }")
        self.close.setText("")
        self.close.setObjectName("close")
        def reduit():
            ajouterevent.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.addevent)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(455, 10, 12, 12))
        self.reduit.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 170, 0);\n"
"    border-radius: 6px;\n"
"   border: none;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 255, 0);\n"
" }")
        self.reduit.setText("")
        self.reduit.setObjectName("reduit")
        self.titre = QtWidgets.QLineEdit(self.addevent)
        self.titre.setGeometry(QtCore.QRect(60, 50, 391, 31))
        self.titre.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.titre.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.titre.setObjectName("titre")
        self.description = QtWidgets.QTextEdit(self.addevent)
        self.description.setGeometry(QtCore.QRect(270, 150, 181, 191))
        self.description.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.description.setObjectName("description")
        self.addannonce = QtWidgets.QLabel(self.addevent)
        self.addannonce.setGeometry(QtCore.QRect(60, 300, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.addannonce.setFont(font)
        self.addannonce.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(255, 255, 127);\n"
"}\n"
"")
        self.addannonce.setObjectName("addannonce")
        self.ajouter = QtWidgets.QPushButton(self.addevent)
        self.ajouter.setGeometry(QtCore.QRect(160, 390, 181, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ajouter.setFont(font)
        self.ajouter.setStyleSheet("QPushButton {\n"
"    color: white;\n"
"    text-shadow: 0 1px 0 rgba(0, 0, 0, 0.4);\n"
"    background: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0 #FF6961, stop: 1 #FFD700);\n"
"    border: 0;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    text-shadow: 0 2px 0 rgba(0, 0, 0, 0.9);\n"
"    background: qradialgradient(cx: 1.5, cy: 0.5, radius: 1.5, fx: 1.5, fy: 0.5, stop: 0.5 #FFD700, stop: 1.5 #FF69B4);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0 #32CD32, stop: 1 #4682B4);\n"
"}\n"
"")
        self.ajouter.setObjectName("ajouter")
        self.label_3 = QtWidgets.QLabel(self.addevent)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 71, 21))
        self.label_3.setStyleSheet("background-color: none;\n"
"color: rgb(72, 72, 36);")
        self.label_3.setObjectName("label_3")
        self.capacitai = QtWidgets.QLineEdit(self.addevent)
        self.capacitai.setGeometry(QtCore.QRect(60, 100, 91, 31))
        self.capacitai.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.capacitai.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.capacitai.setObjectName("capacitai")
        self.prix = QtWidgets.QLineEdit(self.addevent)
        self.prix.setGeometry(QtCore.QRect(180, 100, 91, 31))
        self.prix.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.prix.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.prix.setObjectName("prix")
        self.label = QtWidgets.QLabel(self.addevent)
        self.label.setGeometry(QtCore.QRect(280, 110, 21, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:none;\n"
"")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.addevent)
        self.label_4.setGeometry(QtCore.QRect(70, 150, 71, 21))
        self.label_4.setStyleSheet("background-color: none;\n"
"color: rgb(72, 72, 36);")
        self.label_4.setObjectName("label_4")
        self.Temps = QtWidgets.QComboBox(self.addevent)
        self.Temps.setGeometry(QtCore.QRect(120, 150, 91, 22))
        self.Temps.setObjectName("Temps")
        self.Temps.addItem("")
        self.Temps.addItem("")
        self.Temps.addItem("")
        self.Temps.addItem("")
        self.Temps.addItem("")
        self.Day = QtWidgets.QComboBox(self.addevent)
        self.Day.setGeometry(QtCore.QRect(120, 190, 91, 22))
        self.Day.setObjectName("Day")
        self.Day.addItem("")
        self.Day.addItem("")
        self.Day.addItem("")
        self.Day.addItem("")
        self.Day.addItem("")
        self.Day.addItem("")
        self.Day.addItem("")
        self.label_5 = QtWidgets.QLabel(self.addevent)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 71, 21))
        self.label_5.setStyleSheet("background-color: none;\n"
"color: rgb(72, 72, 36);")
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.addevent)
        self.dateEdit.setGeometry(QtCore.QRect(70, 260, 141, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(ajouterevent)
        QtCore.QMetaObject.connectSlotsByName(ajouterevent)
        self.addannonce.mousePressEvent = self.select_file

        self.ajouter.clicked.connect(self.ajouter_event)

    def retranslateUi(self, ajouterevent):
        _translate = QtCore.QCoreApplication.translate
        ajouterevent.setWindowTitle(_translate("ajouterevent", "Form"))
        self.titre.setPlaceholderText(_translate("ajouterevent", "Saisie Titre"))
        self.description.setPlaceholderText(_translate("ajouterevent", "Déscription"))
        self.addannonce.setText(_translate("ajouterevent", "       Saisir l\'annonce"))
        self.ajouter.setText(_translate("ajouterevent", "Ajouter"))
        self.label_3.setText(_translate("ajouterevent", "Joure"))
        self.capacitai.setPlaceholderText(_translate("ajouterevent", "Saisie Capacité"))
        self.prix.setPlaceholderText(_translate("ajouterevent", "Saisie Prix"))
        self.label.setText(_translate("ajouterevent", "DH"))
        self.label_4.setText(_translate("ajouterevent", "Temps"))
        self.Temps.setItemText(0, _translate("ajouterevent", "00-03h"))
        self.Temps.setItemText(1, _translate("ajouterevent", "05-08h"))
        self.Temps.setItemText(2, _translate("ajouterevent", "10-13h"))
        self.Temps.setItemText(3, _translate("ajouterevent", "15-18h"))
        self.Temps.setItemText(4, _translate("ajouterevent", "20-23h"))
        self.Day.setItemText(0, _translate("ajouterevent", "Lundi"))
        self.Day.setItemText(1, _translate("ajouterevent", "Mardi"))
        self.Day.setItemText(2, _translate("ajouterevent", "Mercredi"))
        self.Day.setItemText(3, _translate("ajouterevent", "Jeudi"))
        self.Day.setItemText(4, _translate("ajouterevent", "Vendredi"))
        self.Day.setItemText(5, _translate("ajouterevent", "Samedi"))
        self.Day.setItemText(6, _translate("ajouterevent", "Dimanche"))
        self.label_5.setText(_translate("ajouterevent", "Date"))

    def select_file(self, event):
         if event.button() == Qt.LeftButton:
              file = QFileDialog()
              file.setNameFilter("Image (*.pdf *.png *.bmp *.gif *.tiff)")
              if file.exec_():
                   try:
                        path = file.selectedFiles()[0]
                        print("path: ", path)
                        self.addannonce_path = path
                        self.addannonce.setStyleSheet("color: green")
                   except Exception as error:
                        print(f"Error: ",error)

    def ajouter_event(self):
        try:
                titre = self.titre.text()
                description = self.description.toPlainText()  
                date = self.dateEdit.date().toString("yyyy-MM-dd")
                day = self.Day.currentText()
                temps = self.Temps.currentText()
                capacitee = self.capacitai.text()
                prix = self.prix.text()
                fichier = self.addannonce_path

                conn = connection.connection
                cursor = conn.cursor()

                query = "INSERT INTO event (titre, description, jour, heur, date, annonce, capaciter, prix) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"

        
                cursor.execute(query, (titre, description, day, temps, date, fichier, capacitee, prix))
                conn.commit()
                cursor.close()
                conn.close()
                self.addevent.close()
        except Exception as e:
                print("Error:", e)
                print("Values:", titre, description, day, temps, date, fichier, capacitee, prix)

        self.addevent.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ajouterevent = QtWidgets.QWidget()
    ui = Ui_ajouterevent()
    ui.setupUi(ajouterevent)
    ajouterevent.show()
    sys.exit(app.exec_())
