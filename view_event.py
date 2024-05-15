from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection
import os

class Ui_view_event(object):
    def setupUi(self, view_event):
        view_event.setObjectName("view_event")
        view_event.resize(526, 607)
        view_event.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        view_event.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.addevent = QtWidgets.QWidget(view_event)
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
            view_event.showMinimized()
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
        self.comboBox = QtWidgets.QComboBox(self.addevent)
        self.comboBox.setGeometry(QtCore.QRect(120, 150, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.addevent)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 190, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.addevent)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 71, 21))
        self.label_5.setStyleSheet("background-color: none;\n"
"color: rgb(72, 72, 36);")
        self.label_5.setObjectName("label_5")
        self.dateEdit = QtWidgets.QDateEdit(self.addevent)
        self.dateEdit.setGeometry(QtCore.QRect(70, 260, 141, 22))
        self.dateEdit.setObjectName("dateEdit")

        self.retranslateUi(view_event)
        QtCore.QMetaObject.connectSlotsByName(view_event)
        self.addannonce.mousePressEvent = self.select_file

        self.ajouter.clicked.connect(self.update)

        self.selected_file_path = None

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

    def retranslateUi(self, view_event):
        self.affiche(self.titre, self.dateEdit)
        _translate = QtCore.QCoreApplication.translate
        view_event.setWindowTitle(_translate("view_event", "Form"))
        self.titre.setPlaceholderText(_translate("view_event", "Saisie Titre"))
        self.description.setPlaceholderText(_translate("view_event", "Déscription"))
        self.addannonce.setText(_translate("view_event", "       Saisir l\'annonce"))
        self.ajouter.setText(_translate("view_event", "Modifier"))
        self.label_3.setText(_translate("view_event", "Joure"))
        self.capacitai.setPlaceholderText(_translate("view_event", "Saisie Capacité"))
        self.prix.setPlaceholderText(_translate("view_event", "Saisie Prix"))
        self.label.setText(_translate("view_event", "DH"))
        self.label_4.setText(_translate("view_event", "Temps"))
        self.comboBox.setItemText(0, _translate("view_event", "00-03h"))
        self.comboBox.setItemText(1, _translate("view_event", "05-08h"))
        self.comboBox.setItemText(2, _translate("view_event", "10-13h"))
        self.comboBox.setItemText(3, _translate("view_event", "15-18h"))
        self.comboBox.setItemText(4, _translate("view_event", "20-23h"))
        self.comboBox_2.setItemText(0, _translate("view_event", "Lundi"))
        self.comboBox_2.setItemText(1, _translate("view_event", "Mardi"))
        self.comboBox_2.setItemText(2, _translate("view_event", "Mercredi"))
        self.comboBox_2.setItemText(3, _translate("view_event", "Jeudi"))
        self.comboBox_2.setItemText(4, _translate("view_event", "Vendredi"))
        self.comboBox_2.setItemText(5, _translate("view_event", "Samedi"))
        self.comboBox_2.setItemText(6, _translate("view_event", "Dimanche"))
        self.label_5.setText(_translate("view_event", "Date"))

    def affiche(self, titre, date):  
        try:    
                conn = connection.connection
                cursor = conn.cursor()

                query = "SELECT titre, description, jour, heur, date, annonce, capaciter, prix FROM event WHERE titre = ? AND date = ?;"  

                cursor.execute(query, (titre, date))
                result = cursor.fetchone()

                if result:
                    self.titre.setText(result[0])
                    self.description.setText(result[1])
                    self.comboBox_2.setCurrentText(result[2])
                    self.comboBox.setCurrentText(result[3])
                    self.dateEdit.setDate(QDate.fromString(result[4], "yyyy-MM-dd"))
                    self.capacitai.setText(str(result[6]))
                    self.prix.setText(str(result[7]))

            # Affichage de l'image
            # Par exemple:
            # path = result[5]
            # pixmap = QPixmap(path)
            # self.addannonce.setPixmap(pixmap)

                cursor.close()
        except Exception as error:
                print("Erreur:", error)

    def update(self):
        try:
                titre = self.titre.text()
                dateEdit = self.dateEdit.date().toString("yyyy-MM-dd")
                description = self.description.toPlainText()
                comboBox_2 = self.comboBox_2.currentText()
                comboBox = self.comboBox.currentText()
                capacitai = self.capacitai.text()
                prix = self.prix.text()

                path = self.selected_file_path
                
                conn = connection.connection
                cursor = conn.cursor()
                query = "UPDATE event SET titre = ?, description = ?, jour = ?, heur = ?, date = ?, annonce = ?, capaciter = ?, prix = ? WHERE titre = ? AND date = ?;"
                values = (titre, description, comboBox_2, comboBox, dateEdit, path, capacitai, prix, titre, dateEdit)
                cursor.execute(query, values)

                conn.commit()
                print("Update successful")
        except Exception as error:
                print("Erreur:", error)
        finally:
                cursor.close()
                conn.close()
                self.addevent.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    view_event = QtWidgets.QWidget()
    ui = Ui_view_event()
    ui.setupUi(view_event)
    view_event.show()
    sys.exit(app.exec_())
