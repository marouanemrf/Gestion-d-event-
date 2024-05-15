from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection

class Recherch(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()

class Ui_vist(object):
    
    def __init__(self):
        super().__init__()
        self.recherche_manager = Recherch()

    def setupUi(self, vist):
        vist.setObjectName("vist")
        vist.resize(925, 542)
        vist.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        vist.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.visiteur_w = QtWidgets.QWidget(vist)
        self.visiteur_w.setGeometry(QtCore.QRect(30, 30, 851, 451))
        self.visiteur_w.setStyleSheet("background-color: rgb(255, 240, 240);\n"
"border-radius: 6px;")
        self.visiteur_w.setObjectName("visiteur_w")
        self.menu = QtWidgets.QLabel(self.visiteur_w)
        self.menu.setGeometry(QtCore.QRect(0, -1, 261, 451))
        self.menu.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); ")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.titre = QtWidgets.QLabel(self.visiteur_w)
        self.titre.setGeometry(QtCore.QRect(110, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.titre.setObjectName("titre")
        self.pic = QtWidgets.QLabel(self.visiteur_w)
        self.pic.setGeometry(QtCore.QRect(10, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pic.setFont(font)
        self.pic.setStyleSheet("border-radius:50px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.nom = QtWidgets.QLabel(self.visiteur_w)
        self.nom.setGeometry(QtCore.QRect(120, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nom.setFont(font)
        self.nom.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.nom.setObjectName("nom")
        self.salut = QtWidgets.QLabel(self.visiteur_w)
        self.salut.setGeometry(QtCore.QRect(110, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.salut.setFont(font)
        self.salut.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.salut.setObjectName("salut")
        self.bord = QtWidgets.QPushButton(self.visiteur_w)
        self.bord.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\dashboard.png'))
        self.bord.setGeometry(QtCore.QRect(0, 200, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bord.setFont(font)
        self.bord.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.bord.setObjectName("bord")
        self.event = QtWidgets.QPushButton(self.visiteur_w)
        self.event.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\event.png'))
        self.event.setGeometry(QtCore.QRect(0, 243, 261, 41))
        self.event.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.event.setFont(font)
        self.event.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.event.setObjectName("event")
        self.participent = QtWidgets.QPushButton(self.visiteur_w)
        self.participent.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\group.png'))
        self.participent.setGeometry(QtCore.QRect(0, 286, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.participent.setFont(font)
        self.participent.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.participent.setObjectName("participent")
        self.visiteur = QtWidgets.QPushButton(self.visiteur_w)
        self.visiteur.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\visitor.png'))
        self.visiteur.setGeometry(QtCore.QRect(0, 329, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.visiteur.setFont(font)
        self.visiteur.setStyleSheet("border-radius: 0px;")
        self.visiteur.setObjectName("visiteur")
        self.recherche = QtWidgets.QLineEdit(self.visiteur_w)
        self.recherche.setGeometry(QtCore.QRect(400, 20, 326, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.cam = QtWidgets.QPushButton(self.visiteur_w)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\camera.png'))
        self.cam.setGeometry(QtCore.QRect(740, 5, 50, 50))
        self.cam.setText("")
        self.cam.setObjectName("cam")
        def reduit():
            vist.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.visiteur_w)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(814, 10, 12, 12))
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
        self.close = QtWidgets.QPushButton(self.visiteur_w)
        self.close.clicked.connect(exit)
        self.close.setGeometry(QtCore.QRect(830, 10, 12, 12))
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
        self.Terminer = QtWidgets.QPushButton(self.visiteur_w)
        self.Terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\exit.png'))
        self.Terminer.setGeometry(QtCore.QRect(0, 370, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Terminer.setFont(font)
        self.Terminer.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.Terminer.setObjectName("Terminer")
        self.list_visiteur = QtWidgets.QTableWidget(self.visiteur_w)
        self.list_visiteur.setGeometry(QtCore.QRect(310, 160, 501, 271))
        self.list_visiteur.setObjectName("list_visiteur")
        self.list_visiteur.setColumnCount(5)
        self.list_visiteur.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.list_visiteur.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_visiteur.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_visiteur.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_visiteur.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_visiteur.setHorizontalHeaderItem(4, item)
        self.ajouter = QtWidgets.QPushButton(self.visiteur_w)
        self.ajouter.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\add.png')) 
        self.ajouter.setGeometry(QtCore.QRect(690, 110, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ajouter.setFont(font)
        self.ajouter.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.ajouter.setObjectName("ajouter")

        self.retranslateUi(vist)
        QtCore.QMetaObject.connectSlotsByName(vist)
        self.recherche_manager.rechercheChange.connect(self.recherche_)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)

        self.bord.clicked.connect(lambda: self.open_dash(self.username, self.pic_path))
        self.event.clicked.connect(lambda: self.open_event(self.username, self.pic_path))
        self.participent.clicked.connect(lambda: self.open_emp(self.username, self.pic_path))
        self.Terminer.clicked.connect(self.open_terminer)
        self.cam.clicked.connect(self.open_cam)
        self.ajouter.clicked.connect(self.add_clt)
        
        self.select_clt()
        self.username = None
        self.pic_path = None

    def set_user_info(self, username, pic_path):
         self.username = username
         self.pic_path = pic_path
         self.update_user_info()

    def update_user_info(self):
         if self.username:
              self.nom.setText(self.username)
         if self.pic_path:
              print("pic path: ", self.pic_path)
              pixmap = QPixmap(self.pic_path)
              pixmap = pixmap.scaled(100, 100)
              pixmap = self.cercle(pixmap)
              self.pic.setPixmap(pixmap)

    def cercle(self, pixmap):
        size = pixmap.size()
        mask = QPixmap(size)
        mask.fill(Qt.transparent)

        painter = QPainter(mask)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.black)
        painter.drawEllipse(0, 0, size.width(), size.height())
        painter.end()

        result = QPixmap(size)
        result.fill(Qt.transparent)

        painter.begin(result)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setCompositionMode(QPainter.CompositionMode_Source)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)
        painter.drawPixmap(0, 0, mask)
        painter.end()

        return result

    def retranslateUi(self, vist):
        _translate = QtCore.QCoreApplication.translate
        vist.setWindowTitle(_translate("vist", "Form"))
        self.titre.setText(_translate("vist", "Gestion des Evenement"))
        self.nom.setText(_translate("vist", "NOM"))
        self.salut.setText(_translate("vist", "Bonjour M/Me"))
        self.bord.setText(_translate("vist", "Table De Bord"))
        self.event.setText(_translate("vist", "Evenement    "))
        self.participent.setText(_translate("vist", "Participent     "))
        self.visiteur.setText(_translate("vist", "Visiteur         "))
        self.recherche.setPlaceholderText(_translate("vist", "Rechercher ici ..."))
        self.Terminer.setText(_translate("vist", "Términer       "))
        item = self.list_visiteur.horizontalHeaderItem(0)
        item.setText(_translate("vist", "Photo"))
        item = self.list_visiteur.horizontalHeaderItem(1)
        item.setText(_translate("vist", "CIN"))
        item = self.list_visiteur.horizontalHeaderItem(2)
        item.setText(_translate("vist", "Nom"))
        item = self.list_visiteur.horizontalHeaderItem(3)
        item.setText(_translate("vist", "Email"))
        item = self.list_visiteur.horizontalHeaderItem(4)
        item.setText(_translate("vist", "Action"))
        self.ajouter.setText(_translate("vist", "Ajouter"))

    def recherche_(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        if text.strip() == "":  
           self.select_clt() 
           return

        query = "SELECT cin, nom, email FROM visiteur WHERE cin LIKE ? OR nom LIKE ? OR email LIKE ? ;"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text, search_text, search_text))
        table = cursor.fetchall()
        
        self.list_visiteur.setRowCount(len(table))

    def select_clt(self):
        conn = connection.connection        
        cursor = conn.cursor()
        query = """
        SELECT photo, cin, nom, email FROM visiteur;
        """     
        cursor.execute(query)
        clt = cursor.fetchall()
        
        self.list_visiteur.setRowCount(len(clt))

        for row, clt_data in enumerate(clt):
                photo_path = clt_data[0]  # Assuming the photo_path is stored in the first column
                cin = clt_data[1]
                nom = clt_data[2]
                email = clt_data[3]

                image_widget = QtWidgets.QLabel()
                image_widget.setStyleSheet("background-color: transparent;")  # Définir un fond rond
                image_widget.resize(30, 30)
                pixmap = QtGui.QPixmap(photo_path)
                pixmap = pixmap.scaled(30, 30)  # Réduire la taille de l'image pour l'afficher correctement
                pixmap = self.cercle(pixmap)
                image_widget.setPixmap(pixmap)

                # Centrer l'image dans la cellule de la colonne
                image_widget.setAlignment(QtCore.Qt.AlignCenter) 

                cin_item = QTableWidgetItem(str(cin))
                nom_item = QTableWidgetItem(nom)
                email_item = QTableWidgetItem(email)

                # Supprimer le widget précédent de la cellule
                previous_widget = self.list_visiteur.cellWidget(row, 0)
                if previous_widget:
                        previous_widget.deleteLater()

                # Set Qlist_visiteurItem to the table widget
                self.list_visiteur.setCellWidget(row, 0, image_widget)  # Utiliser setCellWidget pour définir le widget dans la cellule
                self.list_visiteur.setItem(row, 1, cin_item)
                self.list_visiteur.setItem(row, 2, nom_item)
                self.list_visiteur.setItem(row, 3, email_item)

                # Add buttons to the last column
                widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(widget)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)

                view_button = QPushButton()
                view_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\ticket.png'))
                view_button.setStyleSheet("background-color: none; border: none;")
                view_button.clicked.connect(self.ticket)

                delete_button = QPushButton() 
                delete_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\bin.png'))
                delete_button.setStyleSheet("background-color: none; border: none;")
                delete_button.clicked.connect(self.delete_clt)

                layout.addWidget(view_button)
                layout.addWidget(delete_button)

                self.list_visiteur.setCellWidget(row, 4, widget)

    def ticket(self):
        from ticket import Ui_Form 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_Form()

        self.work.setupUi(self.work_window)
        self.work_window.show()

        line = self.list_visiteur.currentRow()
        cin_item = self.list_visiteur.item(line, 1) 
        print("cin_item: ", cin_item)

        if cin_item is not None:
                cin = cin_item.text()
                print("cin: ", cin)
                self.work.afficher(cin)

    
    def delete_clt(self):
        try: 
             line = self.list_visiteur.currentRow()
             if line != -1:
                  cin_item = self.list_visiteur.item(line, 1)
                  print("cin: ", cin_item)
                  if cin_item is not None:
                       cin = cin_item.text()
                       print("cin: ", cin)
                       conn = connection.connection
                       cursor = conn.cursor()
                       query = "DELETE FROM visiteur WHERE cin = ?;"
                       cursor.execute(query, (cin,))
                       conn.commit()
                       self.select_clt()

        except Exception as e:
             print("erreur: ", e)

    def add_clt(self):
        from add_clt import  Ui_add_Clt
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_add_Clt()

        self.work.setupUi(self.work_window)
        self.work_window.show()

        def close():
             self.work_window.close()
        self.select_clt()
        self.work.close.clicked.connect(close)

    def open_dash(self, username, pic_path):
        from dash import Ui_dash 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_dash()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.visiteur_w.hide()  

    def open_event(self, username, pic_path):
        from event import Ui_event 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_event()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.visiteur_w.hide()      
    
    def open_emp(self, username, pic_path):
        from emp import Ui_emp 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_emp()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.visiteur_w.hide() 
    
    def open_terminer(self):
        from close import Ui_quitter 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_quitter()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def hide():
            self.visiteur_w.close()
            self.work_window.close()
        self.work.oui.clicked.connect(hide) 
        def close():
            self.work_window.close()
        self.work.non.clicked.connect(close)
    
    def open_cam(self):
        from camera import Ui_cam 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_cam()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def close():
            self.work_window.hide()
            self.work.cap.release()

        self.work.close.clicked.connect(close)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    vist = QtWidgets.QWidget()
    ui = Ui_vist()
    ui.setupUi(vist)
    vist.show()
    sys.exit(app.exec_())
