from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from datetime import datetime
import connection
import xlsxwriter
import os


class Recherch(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()

class Ui_event(object):
    def __init__(self):
        super().__init__()
        self.recherche_manager = Recherch() 
    def setupUi(self, event):
        event.setObjectName("event")
        event.resize(927, 538)
        event.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        event.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
        self.event_w = QtWidgets.QWidget(event)
        self.event_w.setGeometry(QtCore.QRect(20, 30, 851, 451))
        self.event_w.setStyleSheet("background-color: rgb(255, 240, 240);\n"
"border-radius: 6px;")
        self.event_w.setObjectName("event_w")
        self.menu = QtWidgets.QLabel(self.event_w)
        self.menu.setGeometry(QtCore.QRect(0, -1, 261, 451))
        self.menu.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); ")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.titre = QtWidgets.QLabel(self.event_w)
        self.titre.setGeometry(QtCore.QRect(110, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.titre.setObjectName("titre")
        self.pic = QtWidgets.QLabel(self.event_w)
        self.pic.setGeometry(QtCore.QRect(10, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pic.setFont(font)
        self.pic.setStyleSheet("border-radius:50px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.nom = QtWidgets.QLabel(self.event_w)
        self.nom.setGeometry(QtCore.QRect(120, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nom.setFont(font)
        self.nom.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.nom.setObjectName("nom")
        self.salut = QtWidgets.QLabel(self.event_w)
        self.salut.setGeometry(QtCore.QRect(110, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.salut.setFont(font)
        self.salut.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.salut.setObjectName("salut")
        self.bord = QtWidgets.QPushButton(self.event_w)
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
        self.event = QtWidgets.QPushButton(self.event_w)
        self.event.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\event.png'))
        self.event.setGeometry(QtCore.QRect(0, 243, 261, 41))
        self.event.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.event.setFont(font)
        self.event.setStyleSheet("border-radius: 0px;\n"
"")
        self.event.setObjectName("event")
        self.participent = QtWidgets.QPushButton(self.event_w)
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
        self.visiteur = QtWidgets.QPushButton(self.event_w)
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
        self.recherche = QtWidgets.QLineEdit(self.event_w)
        self.recherche.setGeometry(QtCore.QRect(400, 20, 326, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.cam = QtWidgets.QPushButton(self.event_w)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\camera.png'))
        self.cam.setGeometry(QtCore.QRect(740, 5, 50, 50))
        self.cam.setText("")
        self.cam.setObjectName("cam")
        def reduit():
            event.shoxMinimized()
        self.reduit = QtWidgets.QPushButton(self.event_w)
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
        self.close = QtWidgets.QPushButton(self.event_w)
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
        self.terminer = QtWidgets.QPushButton(self.event_w)
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
        self.ajouter = QtWidgets.QPushButton(self.event_w)
        self.ajouter.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\add.png'))
        self.ajouter.setGeometry(QtCore.QRect(720, 90, 101, 31))
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
"}")
        self.ajouter.setObjectName("ajouter")
        self.imprimer = QtWidgets.QPushButton(self.event_w)
        self.imprimer.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\print.png'))
        self.imprimer.setGeometry(QtCore.QRect(610, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.imprimer.setFont(font)
        self.imprimer.setStyleSheet("QPushButton{\n"
"    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: rgb(255, 255, 255);\n"
"    border: None;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(255, 240, 240);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.imprimer.setObjectName("imprimer")
        self.tableWidget = QtWidgets.QTableWidget(self.event_w)
        self.tableWidget.setGeometry(QtCore.QRect(310, 150, 511, 271))
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

        self.retranslateUi(event)
        QtCore.QMetaObject.connectSlotsByName(event)
        self.recherche_manager.rechercheChange.connect(self.recherche_)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)

        self.bord.clicked.connect(lambda: self.open_dash(self.username, self.pic_path))
        self.participent.clicked.connect(lambda: self.open_participent(self.username, self.pic_path))
        self.visiteur.clicked.connect(lambda: self.open_visiteur(self.username, self.pic_path))
        self.terminer.clicked.connect(self.open_terminer)
        self.cam.clicked.connect(self.open_cam)
        self.ajouter.clicked.connect(self.add_event)
        self.imprimer.clicked.connect(self.imprimer_data)

        self.username = None
        self.pic_path = None

        self.dead_line()
        self.select_event()

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

    def retranslateUi(self, event):
        _translate = QtCore.QCoreApplication.translate
        event.setWindowTitle(_translate("event", "Form"))
        self.titre.setText(_translate("event", "Gestion des Evenement"))
        self.nom.setText(_translate("event", "NOM"))
        self.salut.setText(_translate("event", "Bonjour M/Me"))
        self.bord.setText(_translate("event", "Table De Bord"))
        self.event.setText(_translate("event", "Evenement    "))
        self.participent.setText(_translate("event", "Participent     "))
        self.visiteur.setText(_translate("event", "Visiteur         "))
        self.recherche.setPlaceholderText(_translate("event", "Rechercher ici ..."))
        self.terminer.setText(_translate("event", "Términer       "))
        self.ajouter.setText(_translate("event", "Ajouter"))
        self.imprimer.setText(_translate("event", "Imprimer"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("event", "Titre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("event", "Date"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("event", "Jour"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("event", "Heur"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("event", "Action"))

    def open_view(self):
        from view_event import Ui_view_event 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_view_event()

        self.work.setupUi(self.work_window)
        self.work_window.show()

        def close():
                self.work_window.close()

        self.work.close.clicked.connect(close)

        line = self.tableWidget.currentRow()
        titre_item = self.tableWidget.item(line, 0)
        date_item = self.tableWidget.item(line, 1) 
        print("titre_item: ", titre_item, " date_item: ", date_item)

        if titre_item is not None and date_item is not None:
                titre = titre_item.text()
                date = date_item.text()
                self.work.affiche(titre, date)
      
        self.select_event()

    def recherche_(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        if text.strip() == "":  
           self.select_event()  
           return

        query = "SELECT titre, date, jour, heur FROM event WHERE titre LIKE ? OR date LIKE ? OR jour LIKE ? OR heur LIKE ? ;"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text, search_text, search_text, search_text))
        table = cursor.fetchall()
        
        self.tableWidget.setRowCount(len(table))

    def select_event(self):
        try:
                conn = connection.connection
                cursor = conn.cursor()

                query = "SELECT titre, date, jour, heur FROM event"
                cursor.execute(query)
                event = cursor.fetchall()

                self.tableWidget.setRowCount(len(event))

                for row, data in enumerate(event):
                        titre = data[0]
                        date = data[1]
                        jour = data[2]
                        heur = data[3]
                        
                        titre_item = QTableWidgetItem(titre)
                        date_item = QTableWidgetItem(str(date))
                        jour_item = QTableWidgetItem(jour)
                        heur_item = QTableWidgetItem(heur)

                        self.tableWidget.setItem(row, 0, titre_item)
                        self.tableWidget.setItem(row, 1, date_item)
                        self.tableWidget.setItem(row, 2, jour_item)
                        self.tableWidget.setItem(row, 3, heur_item)

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
                        delete_button.clicked.connect(self.delete_event)

                        layout.addWidget(view_button)
                        layout.addWidget(delete_button)

                        self.tableWidget.setCellWidget(row, 4, widget)

        except Exception as e:
                print("Error selecting events:", e)
    
    def delete_event(self):
                try: 
                    line = self.tableWidget.currentRow()
                    if line != -1:
                        titre_item = self.tableWidget.item(line, 0)
                        date_item = self.tableWidget.item(line, 1)

                        if titre_item is not None and date_item is not None:
                                titre = titre_item.text()
                                date = date_item.text()

                                conn = connection.connection
                                cursor = conn.cursor()
                                query = "DELETE FROM event WHERE titre = ? AND date = ?;"
                                cursor.execute(query, (titre, date))
                                conn.commit()

                                self.select_event()
                except Exception as e:
                        print("Error deleting event:", e)

    def dead_line(self):
        try:
                conn = connection.connection
                cursor = conn.cursor()
                query = "DELETE FROM event WHERE date < get_date(); "
                cursor.execute(query, )
                conn.commit()
                self.select_event()
        except Exception as e:
            print("erreur: ", e)


    def imprimer_data(self):

        workbook = xlsxwriter.Workbook(os.path.join('data_event', 'event_data.xlsx'))
        worksheet = workbook.add_worksheet()

        headers = ["Titre", "Date", "Jour", "Heur"]
        for col, header in enumerate(headers):
                worksheet.write(0, col, header)

        for row in range(self.tableWidget.rowCount()):
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item is not None:
                        worksheet.write(row + 1, col, item.text())

        workbook.close()

        print("Data exported to event_data.xlsx")

    def add_event(self):
        from add_event import Ui_ajouterevent 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_ajouterevent()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def close():
             self.work_window.close()
        self.work.close.clicked.connect(close)
        self.select_event()

    def open_dash(self, username, pic_path):
        from dash import Ui_dash 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_dash()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.event_w.hide()  

    def open_participent(self, username, pic_path):
        from emp import Ui_emp 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_emp()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.event_w.hide() 
    
    def open_visiteur(self, username, pic_path):
        from visiteur import Ui_vist 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_vist()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.event_w.hide() 
    
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
    event = QtWidgets.QWidget()
    ui = Ui_event()
    ui.setupUi(event)
    event.show()
    sys.exit(app.exec_())
