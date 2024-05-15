from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection


class Ui_addemp(object):
    def setupUi(self, addemp):
        addemp.setObjectName("addemp")
        addemp.resize(700, 500)
        addemp.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        addemp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.addemp_w = QtWidgets.QWidget(addemp)
        self.addemp_w.setGeometry(QtCore.QRect(120, 40, 461, 341))
        self.addemp_w.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 #FF6961 );\n"
"    border-radius: 10px;\n"
"")
        self.addemp_w.setObjectName("addemp_w")
        self.close = QtWidgets.QPushButton(self.addemp_w)
        self.close.setGeometry(QtCore.QRect(440, 10, 12, 12))
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
            addemp.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.addemp_w)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(426, 10, 12, 12))
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
        self.ajouter = QtWidgets.QPushButton(self.addemp_w)
        self.ajouter.setGeometry(QtCore.QRect(150, 270, 181, 35))
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
        self.cin = QtWidgets.QLineEdit(self.addemp_w)
        self.cin.setGeometry(QtCore.QRect(230, 50, 201, 31))
        self.cin.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cin.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cin.setObjectName("cin")
        self.foncyion = QtWidgets.QLineEdit(self.addemp_w)
        self.foncyion.setGeometry(QtCore.QRect(230, 150, 201, 31))
        self.foncyion.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.foncyion.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.foncyion.setObjectName("foncyion")
        self.nom = QtWidgets.QLineEdit(self.addemp_w)
        self.nom.setGeometry(QtCore.QRect(230, 100, 201, 31))
        self.nom.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nom.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.nom.setObjectName("nom")
        self.pic = QtWidgets.QLabel(self.addemp_w)
        self.pic.setGeometry(QtCore.QRect(40, 80, 120, 120))
        self.pic.setStyleSheet("border-radius: 60px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.email = QtWidgets.QLineEdit(self.addemp_w)
        self.email.setGeometry(QtCore.QRect(230, 200, 201, 31))
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.email.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.email.setObjectName("email")

        self.retranslateUi(addemp)
        QtCore.QMetaObject.connectSlotsByName(addemp)
        self.pic.mousePressEvent = self.select_photo

        self.ajouter.clicked.connect(self.ajouter_emp)

        self.selected_photo_path = None

    def retranslateUi(self, addemp):
        _translate = QtCore.QCoreApplication.translate
        addemp.setWindowTitle(_translate("addemp", "Form"))
        self.ajouter.setText(_translate("addemp", "Ajouter"))
        self.cin.setPlaceholderText(_translate("addemp", "Saisie CIN"))
        self.foncyion.setPlaceholderText(_translate("addemp", "Saisie Fonction"))
        self.nom.setPlaceholderText(_translate("addemp", "Saisie Nom Complet"))
        self.email.setPlaceholderText(_translate("addemp", "Saisie Email"))

    def cercle(self, pixmap):
        diam = min(pixmap.width(), pixmap.height())
        circle = QPixmap(diam, diam)
        circle.fill(Qt.transparent)

        mask = QBitmap(diam, diam)
        mask.fill(Qt.white)

        paint = QPainter(mask)
        paint.setRenderHint(QPainter.Antialiasing, True)
        paint.setBrush(Qt.black)
        paint.drawEllipse(0, 0, diam, diam)
        paint.end()

        pixmap.setMask(mask)

        return pixmap

    def select_photo(self, event):
         if event.button() == Qt.LeftButton:
              file = QFileDialog()
              file.setNameFilter("Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)")
              if file.exec_():
                   try:
                        path = file.selectedFiles()[0]
                        print("path: ", path)
                        self.selected_photo_path = path
                        affiche = QPixmap(path)
                        circule = self.cercle(affiche.scaled(120, 120))
                        self.pic.setPixmap(circule)
                        self.pic.setStyleSheet("border-radius: 60px;")
                   except Exception as error:
                        print(f"Error: ",error)
    
    def ajouter_emp(self):
         cin = self.cin.text()
         nom = self.nom.text()
         email = self.email.text()
         fonction = self.foncyion.text()
         photo = self.selected_photo_path
         print("path0: ", photo)
         try:
              conn = connection.connection
              cursor = conn.cursor()
              query = """INSERT INTO participent (cin, nom, email, fonction, photo) 
VALUES (?, ?, ?, ?, ?)
"""
              cursor.execute(query, (cin, nom, email, fonction, photo))     
              conn.commit()
         except Exception as error:

              print("error: ",error)
         finally:
                self.addemp_w.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addemp = QtWidgets.QWidget()
    ui = Ui_addemp()
    ui.setupUi(addemp)
    addemp.show()
    sys.exit(app.exec_())
