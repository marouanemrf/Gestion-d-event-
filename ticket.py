from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
import barcode
from barcode.writer import ImageWriter
import connection
from uuid import uuid1
import subprocess





class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(869, 505)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(120, 30, 601, 441))
        self.widget.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border-radius: 6px;")
        self.widget.setObjectName("widget")
        self.ticket = QtWidgets.QWidget(self.widget)
        self.ticket.setGeometry(QtCore.QRect(40, 20, 521, 331))
        self.ticket.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));")
        self.ticket.setObjectName("ticket")
        self.label = QtWidgets.QLabel(self.ticket)
        self.label.setGeometry(QtCore.QRect(250, 10, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.ticket)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.ticket)
        self.label_3.setGeometry(QtCore.QRect(220, 120, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.ticket)
        self.label_4.setGeometry(QtCore.QRect(220, 270, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:none;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.ticket)
        self.label_5.setGeometry(QtCore.QRect(220, 170, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:none;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.ticket)
        self.label_6.setGeometry(QtCore.QRect(220, 220, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:none;")
        self.label_6.setObjectName("label_6")
        self.nom = QtWidgets.QLabel(self.ticket)
        self.nom.setGeometry(QtCore.QRect(310, 70, 151, 16))
        self.nom.setStyleSheet("background-color:none;")
        self.nom.setObjectName("nom")
        self.date = QtWidgets.QLabel(self.ticket)
        self.date.setGeometry(QtCore.QRect(310, 120, 151, 16))
        self.date.setStyleSheet("background-color:none;")
        self.date.setObjectName("date")
        self.event = QtWidgets.QLabel(self.ticket)
        self.event.setGeometry(QtCore.QRect(310, 170, 151, 16))
        self.event.setStyleSheet("background-color:none;")
        self.event.setObjectName("event")
        self.heur = QtWidgets.QLabel(self.ticket)
        self.heur.setGeometry(QtCore.QRect(310, 220, 151, 16))
        self.heur.setStyleSheet("background-color:none;")
        self.heur.setObjectName("heur")
        self.prix = QtWidgets.QLabel(self.ticket)
        self.prix.setGeometry(QtCore.QRect(310, 270, 151, 16))
        self.prix.setStyleSheet("background-color:none;\n"
"")
        self.prix.setObjectName("prix")
        self.label_12 = QtWidgets.QLabel(self.ticket)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 141, 331))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.Imprimer = QtWidgets.QPushButton(self.widget)
        self.Imprimer.setGeometry(QtCore.QRect(430, 380, 131, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Imprimer.setFont(font)
        self.Imprimer.setStyleSheet("QPushButton {\n"
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
        self.Imprimer.setObjectName("Imprimer")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.Imprimer.clicked.connect(self.print)

    def afficher(self, cin):
        conn = connection.connection
        cursor = conn.cursor()

        query = """
        SELECT visiteur.nom, event.date AS date, event.heur AS heure, event.titre AS evenement, event.prix AS prix
        FROM visiteur
        INNER JOIN event ON visiteur.event_id = event.id
        WHERE cin = ?
        """

        cursor.execute(query, (cin, ))
        result = cursor.fetchall()

        if result:
                for row in result:
                   nom, date, heure, evenement, prix = row
                   self.nom.setText(nom)
                   self.date.setText(date)
                   self.heur.setText(heure)
                   self.event.setText(str(evenement))
                   self.prix.setText(str(prix))
        else:
                print("Aucun résultat trouvé.")

        self.barcode(cin)

        cursor.close()
        conn.close()

    def barcode(self, cin):

        code = barcode.get('code128', cin, writer=ImageWriter())
        bar_path = "barcode.png"
        code.save(bar_path)

        barcode_image = QImage(bar_path)
        barcode_image = barcode_image.transformed(QTransform().rotate(90))
        pixmap = QPixmap.fromImage(barcode_image)

        self.label_12.setPixmap(pixmap)
    
    def print(self):
      self.Imprimer.hide()

      printer = QPrinter(QPrinter.HighResolution)
      printer.setPageSize(QPrinter.A4)

      printer.setOutputFormat(QPrinter.PdfFormat)

      filename = f"{uuid1()}.pdf"

      printer.setOutputFileName(os.path.join('ticket', filename))

      painter = QPainter()
      painter.begin(printer)

      pixmap = self.ticket.grab()
      painter.drawPixmap(130, 130, pixmap)

      painter.end()

#       os.startfile(filename)
      self.widget.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Event T_I_M_E"))
        self.label_2.setText(_translate("Form", "NOM"))
        self.label_3.setText(_translate("Form", "DATE"))
        self.label_5.setText(_translate("Form", "EVENT"))
        self.label_6.setText(_translate("Form", "HEUR"))
        self.label_4.setText(_translate("Form", "PRIX"))

        self.nom.setText(_translate("Form", "N"))
        self.date.setText(_translate("Form", "N"))
        self.event.setText(_translate("Form", "N"))
        self.heur.setText(_translate("Form", "N"))
        self.prix.setText(_translate("Form", "N"))

        self.Imprimer.setText(_translate("Form", "Imprimer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
