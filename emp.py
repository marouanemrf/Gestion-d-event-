from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import connection


class Recherch(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()

class Ui_emp(object):

    def __init__(self):
        super().__init__()
        self.recherche_manager = Recherch()

    def setupUi(self, emp):
        emp.setObjectName("emp")
        emp.resize(897, 511)
        emp.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        emp.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.emp_w = QtWidgets.QWidget(emp)
        self.emp_w.setGeometry(QtCore.QRect(20, 30, 851, 451))
        self.emp_w.setStyleSheet("background-color: rgb(255, 240, 240);\n"
"border-radius: 6px;")
        self.emp_w.setObjectName("emp_w")
        self.menu = QtWidgets.QLabel(self.emp_w)
        self.menu.setGeometry(QtCore.QRect(0, -1, 261, 451))
        self.menu.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); ")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.titre = QtWidgets.QLabel(self.emp_w)
        self.titre.setGeometry(QtCore.QRect(110, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.titre.setObjectName("titre")
        self.pic = QtWidgets.QLabel(self.emp_w)
        self.pic.setGeometry(QtCore.QRect(10, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pic.setFont(font)
        self.pic.setStyleSheet("border-radius:50px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.nom = QtWidgets.QLabel(self.emp_w)
        self.nom.setGeometry(QtCore.QRect(118, 100, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nom.setFont(font)
        self.nom.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.nom.setObjectName("nom")
        self.salut = QtWidgets.QLabel(self.emp_w)
        self.salut.setGeometry(QtCore.QRect(120, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.salut.setFont(font)
        self.salut.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.salut.setObjectName("salut")
        self.bord = QtWidgets.QPushButton(self.emp_w)
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
"}\n"
"")
        self.bord.setObjectName("bord")
        self.event = QtWidgets.QPushButton(self.emp_w)
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
        self.participent = QtWidgets.QPushButton(self.emp_w)
        self.participent.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\group.png'))
        self.participent.setGeometry(QtCore.QRect(0, 286, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.participent.setFont(font)
        self.participent.setStyleSheet("border-radius: 0px;")
        self.participent.setObjectName("participent")
        self.visiteur = QtWidgets.QPushButton(self.emp_w)
        self.visiteur.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\visitor.png'))
        self.visiteur.setGeometry(QtCore.QRect(0, 329, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.visiteur.setFont(font)
        self.visiteur.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.visiteur.setObjectName("visiteur")
        self.recherche = QtWidgets.QLineEdit(self.emp_w)
        self.recherche.setGeometry(QtCore.QRect(400, 20, 326, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.cam = QtWidgets.QPushButton(self.emp_w)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\camera.png'))
        self.cam.setGeometry(QtCore.QRect(740, 5, 50, 50))
        self.cam.setText("")
        self.cam.setObjectName("cam")
        def reduit():
            emp.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.emp_w)
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
        self.close = QtWidgets.QPushButton(self.emp_w)
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
        self.terminer = QtWidgets.QPushButton(self.emp_w)
        self.terminer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\exit.png'))
        self.terminer.setGeometry(QtCore.QRect(0, 370, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.terminer.setFont(font)
        self.terminer.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.terminer.setObjectName("terminer")
        self.ajouter = QtWidgets.QPushButton(self.emp_w)
        self.ajouter.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\add.png')) 
        self.ajouter.setGeometry(QtCore.QRect(680, 100, 121, 31))
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
        self.tableWidget = QtWidgets.QTableWidget(self.emp_w)
        self.tableWidget.setGeometry(QtCore.QRect(290, 150, 520, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.retranslateUi(emp)
        QtCore.QMetaObject.connectSlotsByName(emp)
        self.recherche_manager.rechercheChange.connect(self.recherche_)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)

        self.bord.clicked.connect(lambda: self.open_dash(self.username, self.pic_path))
        self.event.clicked.connect(lambda: self.open_event(self.username, self.pic_path))
        self.visiteur.clicked.connect(lambda: self.open_visiteur(self.username, self.pic_path))
        self.terminer.clicked.connect(self.open_terminer)
        self.cam.clicked.connect(self.open_cam)
        self.ajouter.clicked.connect(self.add_emp)
        
        self.select_emp()
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

    def retranslateUi(self, emp):
        _translate = QtCore.QCoreApplication.translate
        emp.setWindowTitle(_translate("emp", "Form"))
        self.titre.setText(_translate("emp", "Gestion des Evenement"))
        self.nom.setText(_translate("emp", "NOM"))
        self.salut.setText(_translate("emp", "Bonjour M/Me"))
        self.bord.setText(_translate("emp", "Table De Bord"))
        self.event.setText(_translate("emp", "Evenement    "))
        self.participent.setText(_translate("emp", "Participent     "))
        self.visiteur.setText(_translate("emp", "Visiteur         "))
        self.recherche.setPlaceholderText(_translate("emp", "Rechercher ici ..."))
        self.terminer.setText(_translate("emp", "Términer       "))
        self.ajouter.setText(_translate("emp", "Ajouter"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("emp", "Photo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("emp", "CIN"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("emp", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("emp", "Fonction"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("emp", "Action"))

    def select_emp(self):
        conn = connection.connection        
        cursor = conn.cursor()
        query = """
        SELECT photo, cin, nom, fonction FROM participent;
        """     
        cursor.execute(query)
        emp = cursor.fetchall()
        
        self.tableWidget.setRowCount(len(emp))

        for row, emp_data in enumerate(emp):
                photo_path = emp_data[0]  
                cin = emp_data[1]
                nom = emp_data[2]
                fonction = emp_data[3]

                image_widget = QtWidgets.QLabel()
                image_widget.setStyleSheet("background-color: transparent;")  
                image_widget.resize(30, 30)
                pixmap = QtGui.QPixmap(photo_path)
                pixmap = pixmap.scaled(30, 30)  
                pixmap = self.cercle(pixmap)
                image_widget.setPixmap(pixmap)

                image_widget.setAlignment(QtCore.Qt.AlignCenter) 

                cin_item = QTableWidgetItem(str(cin))
                nom_item = QTableWidgetItem(nom)
                fonction_item = QTableWidgetItem(fonction)

                self.tableWidget.setCellWidget(row, 0, image_widget)  
                self.tableWidget.setItem(row, 1, cin_item)
                self.tableWidget.setItem(row, 2, nom_item)
                self.tableWidget.setItem(row, 3, fonction_item)

                widget = QtWidgets.QWidget()
                layout = QtWidgets.QHBoxLayout(widget)
                layout.setContentsMargins(0, 0, 0, 0)
                layout.setSpacing(0)

                view_button = QPushButton()
                view_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\view.png'))
                view_button.setStyleSheet("background-color: none; border: none;")
                view_button.clicked.connect(self.open_view)

                delete_button = QPushButton() 
                delete_button.setIcon(QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\bin.png'))
                delete_button.setStyleSheet("background-color: none; border: none;")
                delete_button.clicked.connect(self.delete_emp)

                layout.addWidget(view_button)
                layout.addWidget(delete_button)

                self.tableWidget.setCellWidget(row, 4, widget)


    def open_view(self):
        from view_emp import Ui_viewEmp 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_viewEmp()

        self.work.setupUi(self.work_window)
        self.work_window.show()

        def close():
                self.work_window.close()

        self.work.close.clicked.connect(close)

        line = self.tableWidget.currentRow()
        cin_item = self.tableWidget.item(line, 1) 
        print("cin_item: ", cin_item)

        if cin_item is not None:
                cin = cin_item.text()
                print("cin: ", cin)
                self.work.affiche(cin)
                self.select_emp()

    
    def delete_emp(self):
        try: 
             line = self.tableWidget.currentRow()
             if line != -1:
                  cin_item = self.tableWidget.item(line, 1)
                  print("cin: ", cin_item)
                  if cin_item is not None:
                       cin = cin_item.text()
                       print("cin: ", cin)
                       conn = connection.connection
                       cursor = conn.cursor()
                       query = "DELETE FROM participent WHERE cin = ?;"
                       cursor.execute(query, (cin,))
                       conn.commit()
                       self.select_emp()
        except Exception as e:
             print("erreur: ", e)

    def recherche_(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        if text.strip() == "":  
           self.select_emp() 
           return

        query = "SELECT photo, cin, nom, fonction FROM participent WHERE cin LIKE ? OR nom LIKE ? OR fonction LIKE ? ;"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text, search_text, search_text))
        table = cursor.fetchall()
        
        self.tableWidget.setRowCount(len(table))

    def add_emp(self):
        from add_emp import Ui_addemp 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_addemp()

        self.work.setupUi(self.work_window)
        self.work_window.show()

        def close():
             self.work_window.close()

        self.work.close.clicked.connect(close)



    def open_dash(self, username, pic_path):
        from dash import Ui_dash 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_dash()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.emp_w.hide()  

    def open_event(self, username, pic_path):
        from event import Ui_event 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_event()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.emp_w.hide()      
    
    def open_visiteur(self, username, pic_path):
        from visiteur import Ui_vist 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_vist()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.emp_w.hide() 
    
    def open_terminer(self):
        from close import Ui_quitter 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_quitter()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def hide():
            self.event_w.close()
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
    emp = QtWidgets.QWidget()
    ui = Ui_emp()
    ui.setupUi(emp)
    emp.show()
    sys.exit(app.exec_())