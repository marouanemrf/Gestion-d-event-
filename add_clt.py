from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection


class Ui_add_Clt(object):
    def setupUi(self, add_Clt):
        add_Clt.setObjectName("add_Clt")
        add_Clt.resize(790, 527)
        add_Clt.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        add_Clt.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.addClt_w = QtWidgets.QWidget(add_Clt)
        self.addClt_w.setGeometry(QtCore.QRect(160, 70, 461, 331))
        self.addClt_w.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 #FF6961 );\n"
"    border-radius: 10px;\n"
"")
        self.addClt_w.setObjectName("addClt_w")
        self.close = QtWidgets.QPushButton(self.addClt_w)
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
            add_Clt.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.addClt_w)
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
        self.ajouter = QtWidgets.QPushButton(self.addClt_w)
        self.ajouter.setGeometry(QtCore.QRect(140, 260, 181, 35))
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
        self.cin = QtWidgets.QLineEdit(self.addClt_w)
        self.cin.setGeometry(QtCore.QRect(220, 40, 201, 31))
        self.cin.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cin.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cin.setObjectName("cin")
        self.nom = QtWidgets.QLineEdit(self.addClt_w)
        self.nom.setGeometry(QtCore.QRect(220, 90, 201, 31))
        self.nom.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nom.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.nom.setObjectName("nom")
        self.pic = QtWidgets.QLabel(self.addClt_w)
        self.pic.setGeometry(QtCore.QRect(30, 70, 141, 141))
        self.pic.setStyleSheet("border-radius: 70px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.email = QtWidgets.QLineEdit(self.addClt_w)
        self.email.setGeometry(QtCore.QRect(220, 140, 201, 31))
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.email.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.email.setObjectName("email")
        self.comboBox = QtWidgets.QComboBox(self.addClt_w)
        self.comboBox.setGeometry(QtCore.QRect(220, 210, 201, 22))
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.addClt_w)
        self.label.setGeometry(QtCore.QRect(220, 190, 111, 16))
        self.label.setStyleSheet("background-color: none;\n"
"color: rgb(58, 58, 43);")
        self.label.setObjectName("label")

        self.retranslateUi(add_Clt)
        QtCore.QMetaObject.connectSlotsByName(add_Clt)
        self.pic.mousePressEvent = self.select_photo

        self.ajouter.clicked.connect(self.ajouter_clt)

        self.selected_photo_path = None

        self.select = self.event_select()


    def retranslateUi(self, add_Clt):
        _translate = QtCore.QCoreApplication.translate
        add_Clt.setWindowTitle(_translate("add_Clt", "add_Clt"))
        self.ajouter.setText(_translate("add_Clt", "Ajouter"))
        self.cin.setPlaceholderText(_translate("add_Clt", "Saisie CIN"))
        self.nom.setPlaceholderText(_translate("add_Clt", "Saisie Nom Complet"))
        self.email.setPlaceholderText(_translate("add_Clt", "Saisie Email"))
        self.label.setText(_translate("add_Clt", "Choix D\'Evenemnt"))

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
                        circule = self.cercle(affiche.scaled(141, 141))
                        self.pic.setPixmap(circule)
                        self.pic.setStyleSheet("border-radius: 70px;")
                   except Exception as error:
                        print(f"Error: ",error)

    def ajouter_clt(self):
        conn = connection.connection
        cursor = conn.cursor()

        cin = self.cin.text()
        nom = self.nom.text()
        email = self.email.text()
        photo = self.selected_photo_path
        titre_evenement = self.comboBox.currentText()  

        query_select = "SELECT id FROM event WHERE titre = ?"
        cursor.execute(query_select, (titre_evenement,))
        row = cursor.fetchone()  

        if row is not None:
            event_id = row[0]  
            try:
                event_id = int(event_id)
            except ValueError:
                QMessageBox.warning(self, "Erreur", "L'ID de l'événement n'est pas un entier valide.")
                return
        else:
            QMessageBox.warning(self, "Erreur", "Aucun événement trouvé avec ce titre.")
            return

        query_insert = """INSERT INTO visiteur (cin, nom, email, photo, event_id) 
                          VALUES (?, ?, ?, ?, ?);
                       """
        try:
            cursor.execute(query_insert, (cin, nom, email, photo, event_id))
            conn.commit()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de l'ajout du client : {str(e)}")
        finally:
            self.addClt_w.close()


    def event_select(self):
        conn = connection.connection
        cursor = conn.cursor()
        
        query = """
    SELECT titre 
    FROM event 
    WHERE capaciter > (SELECT count(*) FROM visiteur WHERE event_id = event.id);
"""
        cursor.execute(query)
        titles = cursor.fetchall()

        for title in titles:
            self.comboBox.addItem(title[0])                   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    add_Clt = QtWidgets.QWidget()
    ui = Ui_add_Clt()
    ui.setupUi(add_Clt)
    add_Clt.show()
    sys.exit(app.exec_())
