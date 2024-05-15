from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import connection

class Recherch(QObject):
    rechercheChange = pyqtSignal(str)
    def __init__(self):
        super().__init__()

class Ui_dash(object):
    def __init__(self):
        super().__init__()
        self.recherche_manager = Recherch() 

    def setupUi(self, dash):
        dash.setObjectName("dash")
        dash.resize(931, 538)
        dash.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        dash.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.dash_w = QtWidgets.QWidget(dash)
        self.dash_w.setGeometry(QtCore.QRect(40, 40, 851, 451))
        self.dash_w.setStyleSheet("background-color: rgb(255, 240, 240);\n"
"border-radius: 6px;")
        self.dash_w.setObjectName("dash_w")
        self.menu = QtWidgets.QLabel(self.dash_w)
        self.menu.setGeometry(QtCore.QRect(0, -1, 261, 451))
        self.menu.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 rgb(255, 255, 127) );\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); ")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.titre = QtWidgets.QLabel(self.dash_w)
        self.titre.setGeometry(QtCore.QRect(110, 10, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.titre.setObjectName("titre")
        self.pic = QtWidgets.QLabel(self.dash_w)
        self.pic.setGeometry(QtCore.QRect(10, 50, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pic.setFont(font)
        self.pic.setStyleSheet("border-radius:50px;")
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.nom = QtWidgets.QLabel(self.dash_w)
        self.nom.setGeometry(QtCore.QRect(118, 100, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.nom.setFont(font)
        self.nom.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.nom.setObjectName("nom")
        self.salut = QtWidgets.QLabel(self.dash_w)
        self.salut.setGeometry(QtCore.QRect(120, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.salut.setFont(font)
        self.salut.setStyleSheet("background-color:none;\n"
"color: rgb(255, 255, 255);")
        self.salut.setObjectName("salut")
        self.bord = QtWidgets.QPushButton(self.dash_w)
        self.bord.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\dashboard.png'))
        self.bord.setGeometry(QtCore.QRect(0, 200, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bord.setFont(font)
        self.bord.setStyleSheet("border-radius: 0px;\n"
"")
        self.bord.setObjectName("bord")
        self.event = QtWidgets.QPushButton(self.dash_w)
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
        self.participent = QtWidgets.QPushButton(self.dash_w)
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
        self.visiteur = QtWidgets.QPushButton(self.dash_w)
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
        self.terminer = QtWidgets.QPushButton(self.dash_w)
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
        self.recherche = QtWidgets.QLineEdit(self.dash_w)
        self.recherche.setGeometry(QtCore.QRect(400, 20, 326, 20))
        self.recherche.setStyleSheet("                max-width: 300px;\n"
"                padding: 0px 12px; \n"
"                border-radius: 8px;\n"
"                border: 1px solid #000000;\n"
"                outline: none;\n"
"                box-shadow: 0px 0px 20px -18px; ")
        self.recherche.setObjectName("recherche")
        self.label = QtWidgets.QLabel(self.dash_w)
        self.label.setGeometry(QtCore.QRect(290, 80, 111, 101))
        self.label.setStyleSheet("background-color: rgb(255, 255, 178);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.dash_w)
        self.label_2.setGeometry(QtCore.QRect(440, 80, 111, 101))
        self.label_2.setStyleSheet("background-color: rgb(189, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.dash_w)
        self.label_3.setGeometry(QtCore.QRect(590, 80, 111, 101))
        self.label_3.setStyleSheet("background-color:rgb(255, 151, 137);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.dash_w)
        self.label_4.setGeometry(QtCore.QRect(311, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: none;")
        self.label_4.setObjectName("label_4")
        self.nbEvnt = QtWidgets.QLabel(self.dash_w)
        self.nbEvnt.setGeometry(QtCore.QRect(336, 130, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nbEvnt.setFont(font)
        self.nbEvnt.setStyleSheet("background-color: none;")
        self.nbEvnt.setObjectName("nbEvnt")
        self.label_6 = QtWidgets.QLabel(self.dash_w)
        self.label_6.setGeometry(QtCore.QRect(467, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: none;")
        self.label_6.setObjectName("label_6")
        self.nb_part = QtWidgets.QLabel(self.dash_w)
        self.nb_part.setGeometry(QtCore.QRect(490, 130, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nb_part.setFont(font)
        self.nb_part.setStyleSheet("background-color: none;")
        self.nb_part.setObjectName("nb_part")
        self.label_8 = QtWidgets.QLabel(self.dash_w)
        self.label_8.setGeometry(QtCore.QRect(624, 100, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: none;")
        self.label_8.setObjectName("label_8")
        self.nb_vis = QtWidgets.QLabel(self.dash_w)
        self.nb_vis.setGeometry(QtCore.QRect(639, 130, 20, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.nb_vis.setFont(font)
        self.nb_vis.setStyleSheet("background-color: none;")
        self.nb_vis.setObjectName("nb_vis")
        self.cam = QtWidgets.QPushButton(self.dash_w)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\camera.png'))
        self.cam.setGeometry(QtCore.QRect(740, 20, 20, 20))
        self.cam.setText("")
        self.cam.setObjectName("cam")
        self.stat = QtWidgets.QLabel(self.dash_w)
        self.stat.setGeometry(QtCore.QRect(350, 220, 171, 171))
        self.stat.setStyleSheet("background-color: rgb(255, 250, 180);\n"
"border-radius: 80px;")
        self.stat.setText("")
        self.stat.setObjectName("stat")
        self.listadmin = QtWidgets.QTableWidget(self.dash_w)
        self.listadmin.setGeometry(QtCore.QRect(600, 220, 217, 171))
        self.listadmin.setStyleSheet("QTableWidget{\n"
"background-color: rgb(255, 255, 127);\n"
"border-radius: 2px;\n"
"}\n"
"QTableWidget::items{\n"
"background-color:rgb(255, 253, 193);\n"
"}")
        self.listadmin.setObjectName("listadmin")
        self.listadmin.setColumnCount(2)
        self.listadmin.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.listadmin.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.listadmin.setHorizontalHeaderItem(1, item)
        def reduit():
            dash.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.dash_w)
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
        self.close = QtWidgets.QPushButton(self.dash_w)
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

        self.retranslateUi(dash)
        QtCore.QMetaObject.connectSlotsByName(dash)

        self.recherche_manager.rechercheChange.connect(self.recherche_)
        self.recherche.textChanged.connect(self.recherche_manager.rechercheChange.emit)

        self.event.clicked.connect(lambda: self.open_event(self.username, self.pic_path))
        self.participent.clicked.connect(lambda: self.open_participent(self.username, self.pic_path))
        self.visiteur.clicked.connect(lambda: self.open_visiteur(self.username, self.pic_path))
        self.terminer.clicked.connect(self.open_terminer)
        self.cam.clicked.connect(self.open_cam)

        self.username = None
        self.pic_path = None

        self.statistique()
        self.set_admin()
        self.event_count()
        self.visiteur_count()
        self.participent_count() 

    def retranslateUi(self, dash):
        _translate = QtCore.QCoreApplication.translate
        dash.setWindowTitle(_translate("dash", "Form"))
        self.titre.setText(_translate("dash", "Gestion des Evenement"))
        self.nom.setText(_translate("dash", "NOM"))
        self.salut.setText(_translate("dash", "Bonjour M/Me"))
        self.bord.setText(_translate("dash", "Table De Bord"))
        self.event.setText(_translate("dash", "Evenement    "))
        self.participent.setText(_translate("dash", "Participent     "))
        self.visiteur.setText(_translate("dash", "Visiteur         "))
        self.terminer.setText(_translate("dash", "Términer       "))
        self.recherche.setPlaceholderText(_translate("dash", "Rechercher ici ..."))
        self.label_4.setText(_translate("dash", "Evenement"))
        self.nbEvnt.setText(_translate("dash", "5"))
        self.label_6.setText(_translate("dash", "Participent"))
        self.nb_part.setText(_translate("dash", "5"))
        self.label_8.setText(_translate("dash", "Visiteur"))
        self.nb_vis.setText(_translate("dash", "5"))
        item = self.listadmin.horizontalHeaderItem(0)
        item.setText(_translate("dash", "Photo"))
        item = self.listadmin.horizontalHeaderItem(1)
        item.setText(_translate("dash", "Nom"))

    def event_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        count = "SELECT count(*) FROM event;"
        cursor.execute(count)
        result = cursor.fetchone()
        count = int(result[0]) if result else int(0)
        count_str = str(count)  
        self.nbEvnt.setText(count_str)
        return count
    
    def visiteur_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        count = "SELECT count(*) FROM visiteur"
        cursor.execute(count)
        result = cursor.fetchone()
        count = int(result[0]) if result else int(0)
        count_str = str(count) 
        self.nb_vis.setText(count_str)
        return count
    
    def participent_count(self):
        conn = connection.connection
        cursor = conn.cursor()

        count = "SELECT count(*) FROM participent"
        cursor.execute(count)
        result = cursor.fetchone()
        count = int(result[0]) if result else int(0)
        count_str = str(count)
        self.nb_part.setText(count_str)
        return count
    
    def fig_to_pixmap(self, fig):
        buffer = QtCore.QBuffer()
        buffer.open(QtCore.QIODevice.ReadWrite)
        fig.savefig(buffer, format='png', transparent=True)
        pixmap = QtGui.QPixmap()  
        pixmap.loadFromData(buffer.data())
        pixmap = pixmap.scaled(171, 171)
        buffer.close()
        return pixmap
    
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

    def statistique(self):
        event_count = self.event_count()
        participant_count = self.participent_count()
        visiteur_count = self.visiteur_count()

        labels = ['Evenement', 'Participent', 'Visiteur']
        colors = [(255/255, 255/255, 178/255), (189/255, 255/255, 255/255), (255/255, 151/255, 137/255)]  
        size = [event_count, participant_count, visiteur_count]  

        total = sum(size) 

        if total == 0:
                print("Toutes les parts sont nulles. Le diagramme ne peut pas être affiché.")
                return

        stat_width = self.stat.width()
        stat_height = self.stat.height()

        fig, ax = plt.subplots(figsize=(stat_width / 100, stat_height / 100))

        ax.pie(size, autopct='%1.1f%%', startangle=100, colors=colors, wedgeprops={'width': 0.3, 'edgecolor': 'w'})

        plt.rcParams.update({'font.size': 8})

        ax.axis('equal')

        pixmap = self.fig_to_pixmap(fig)

        self.stat.setPixmap(pixmap)

    def set_admin(self):
        conn = connection.connection
        cursor = conn.cursor()

        admin_query = "SELECT nom, photo FROM logevent"

        try:
                cursor.execute(admin_query)

                admins = cursor.fetchall()

                self.listadmin.setRowCount(len(admins))

                for row, admin in enumerate(admins):
                        nom_admin = admin[0] 
                        photo_admin = admin[1]  

                        image_widget = QtWidgets.QLabel()
                        image_widget.setStyleSheet("background-color: transparent;")  
                        image_widget.resize(30, 30)
                        pixmap = QtGui.QPixmap(photo_admin)
                        pixmap = pixmap.scaled(30, 30)  
                        pixmap = self.cercle(pixmap)
                        image_widget.setPixmap(pixmap)

                        image_widget.setAlignment(QtCore.Qt.AlignCenter)


                        self.listadmin.setCellWidget(row, 0, image_widget)


                        self.listadmin.setItem(row, 1, QtWidgets.QTableWidgetItem(nom_admin))

        except Exception as e:
                print("Erreur lors de l'exécution de la requête:", e)

    def recherche_(self, text):
        conn = connection.connection
        cursor = conn.cursor()

        if text.strip() == "":  
           self.set_admin()  
           return

        query = "SELECT nom FROM logevent WHERE nom LIKE ? ;"
        search_text = f"%{text}%"
        cursor.execute(query, (search_text,))
        table = cursor.fetchall()
        
        self.listadmin.setRowCount(len(table))
        
    def open_event(self, username, pic_path):
        from event import Ui_event 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_event()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.dash_w.hide()       

    def open_participent(self, username, pic_path):
        from emp import Ui_emp 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_emp()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.dash_w.hide() 
    
    def open_visiteur(self, username, pic_path):
        from visiteur import Ui_vist 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_vist()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        self.dash_w.hide() 
    
    def open_terminer(self):
        from close import Ui_quitter 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_quitter()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def hide():
            self.dash_w.close()
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
    dash = QtWidgets.QWidget()
    ui = Ui_dash()
    ui.setupUi(dash)
    dash.show()
    sys.exit(app.exec_())
