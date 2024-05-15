from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection
import os

class Ui_viewEmp(object):
    def setupUi(self, viewEmp):
        viewEmp.setObjectName("viewEmp")
        viewEmp.resize(700, 500)
        viewEmp.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        viewEmp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.viewEmp_w = QtWidgets.QWidget(viewEmp)
        self.viewEmp_w.setGeometry(QtCore.QRect(120, 40, 461, 341))
        self.viewEmp_w.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 #FF6961 );\n"
"    border-radius: 10px;\n"
"")
        self.viewEmp_w.setObjectName("viewEmp_w")
        self.close = QtWidgets.QPushButton(self.viewEmp_w)
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
            viewEmp.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.viewEmp_w)
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
        self.ajouter = QtWidgets.QPushButton(self.viewEmp_w)
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
        self.cin = QtWidgets.QLineEdit(self.viewEmp_w)
        self.cin.setGeometry(QtCore.QRect(230, 50, 201, 31))
        self.cin.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.cin.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.cin.setObjectName("cin")
        self.foncyion = QtWidgets.QLineEdit(self.viewEmp_w)
        self.foncyion.setGeometry(QtCore.QRect(230, 150, 201, 31))
        self.foncyion.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.foncyion.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.foncyion.setObjectName("foncyion")
        self.nom = QtWidgets.QLineEdit(self.viewEmp_w)
        self.nom.setGeometry(QtCore.QRect(230, 100, 201, 31))
        self.nom.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.nom.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.nom.setObjectName("nom")
        self.pic = QtWidgets.QLabel(self.viewEmp_w)
        self.pic.setGeometry(QtCore.QRect(40, 80, 120, 120))
        self.pic.setStyleSheet("border-radius: 60px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.imprimer = QtWidgets.QPushButton(self.viewEmp_w)
        self.imprimer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\print.png'))
        self.imprimer.setGeometry(QtCore.QRect(20, 10, 31, 31))
        self.imprimer.setStyleSheet("background-color: none;")
        self.imprimer.setText("")
        self.imprimer.setObjectName("imprimer")
        self.email = QtWidgets.QLineEdit(self.viewEmp_w)
        self.email.setGeometry(QtCore.QRect(230, 200, 201, 31))
        self.email.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.email.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.email.setObjectName("email")

        self.retranslateUi(viewEmp)
        QtCore.QMetaObject.connectSlotsByName(viewEmp)
        self.pic.mousePressEvent = self.select_photo

        self.ajouter.clicked.connect(self.update)
        self.imprimer.clicked.connect(self.print_to_pdf)

        self.selected_photo_path = None

    def retranslateUi(self, viewEmp):
        _translate = QtCore.QCoreApplication.translate
        viewEmp.setWindowTitle(_translate("viewEmp", "Form"))
        self.ajouter.setText(_translate("viewEmp", "Modifier"))
        self.cin.setPlaceholderText(_translate("viewEmp", "Saisie CIN"))
        self.affiche(self.cin)
        self.foncyion.setPlaceholderText(_translate("viewEmp", "Saisie Fonction"))
        self.nom.setPlaceholderText(_translate("viewEmp", "Saisie Nom Complet"))
        self.email.setPlaceholderText(_translate("viewEmp", "Saisie Email"))


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

    def affiche(self, cin):  
        try:    
                conn = connection.connection
                cursor = conn.cursor()

                query = "SELECT cin, nom, email, fonction, photo FROM participent WHERE cin = ?"  

                cursor.execute(query, (cin,))
                result = cursor.fetchone()
                
                if result:
                        self.cin.setText(cin)
                        print("CIN: ", cin)  
                        self.nom.setText(result[1])  
                        self.email.setText(result[2])  
                        self.foncyion.setText(result[3])  
                        photo_path = result[4]

                        if photo_path:
                                affiche = QPixmap(photo_path)
                                circuler = self.cercle(affiche.scaled(120, 120))
                                self.pic.setPixmap(circuler)
                                self.pic.setStyleSheet("border-radius: 60px;")

                cursor.close()        

        except Exception as error:
                print("Erreur:", error)


    def update(self):
         try:
              cin = self.cin.text()
              nom = self.nom.text()
              email = self.email.text()
              fonction = self.foncyion.text()

              photo = self.selected_photo_path
              
              conn = connection.connection
              cursor = conn.cursor()
              query = "UPDATE participent SET cin = ?, nom = ?, email = ?, fonction = ?, photo = ? WHERE cin = ?;"
              values = (cin, nom, email, fonction, photo)
              print("values: ", values)
              cursor.execute(query, (cin, nom, email, fonction, photo, cin))

              conn.commit()
              print("Update successful")
         except Exception as error:
              print("erreur: ",error)
         finally:
              cursor.close()
              conn.close()
              self.viewEmp_w.hide()  

    def print_to_pdf(self):

        self.close.hide()
        self.reduit.hide()
        self.ajouter.hide()
        self.imprimer.hide()

        # Création d'une instance de QPrinter avec une résolution élevée
        printer = QPrinter(QPrinter.HighResolution)
        
        # Ajustement de la taille de la page du printer
        printer.setPageSize(QPrinter.A4)
        
        # Définition du format de sortie du printer en PDF
        printer.setOutputFormat(QPrinter.PdfFormat)
        
        # Obtention du CIN de la personne pour le nom du fichier de sortie
        cin = self.cin.text()
        output_filename = f"{cin}.pdf"  # Utilisation du CIN comme nom de fichier
        
        # Définition du nom du fichier de sortie PDF
        printer.setOutputFileName(os.path.join('badge', output_filename))

        # Création d'une instance QPainter qui va dessiner sur le printer (le PDF)
        painter = QPainter(printer)

        painter.scale(13, 8)

        # Rendu du contenu de self.viewEmp_w sur le QPainter
        self.viewEmp_w.render(painter)

        # Fermeture du QPainter, ce qui finalise le dessin sur le printer
        painter.end()
        self.viewEmp_w.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewEmp = QtWidgets.QWidget()
    ui = Ui_viewEmp()
    ui.setupUi(viewEmp)
    viewEmp.show()
    sys.exit(app.exec_())
