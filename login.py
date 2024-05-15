import connection
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import os
import glob
import face_recognition
import numpy as np
import time


class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName("loginForm")
        loginForm.resize(860, 513)
        loginForm.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        loginForm.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Loginwidget = QtWidgets.QWidget(loginForm)
        self.Loginwidget.setGeometry(QtCore.QRect(130, 60, 591, 361))
        self.Loginwidget.setStyleSheet("    background-color: qradialgradient(cx: 1, cy: 0, radius: 1, fx: 1, fy: 0, stop: 0#FFD700, stop: 1 #FF6961 );\n"
"    color: white;\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); ")
        self.Loginwidget.setObjectName("Loginwidget")
        self.user_name = QtWidgets.QLineEdit(self.Loginwidget)
        self.user_name.setGeometry(QtCore.QRect(350, 130, 211, 31))
        self.user_name.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.user_name.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.user_name.setObjectName("user_name")
        self.password = QtWidgets.QLineEdit(self.Loginwidget)
        self.password.setGeometry(QtCore.QRect(350, 190, 211, 31))
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password.setStyleSheet("background-color: rgba(0,0, 0,0); \n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton(self.Loginwidget)
        self.login.setGeometry(QtCore.QRect(386, 270, 145, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.login.setFont(font)
        self.login.setStyleSheet("QPushButton {\n"
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
        self.login.setObjectName("login")
        self.cam = QtWidgets.QPushButton(self.Loginwidget)
        self.cam.setIcon(QtGui.QIcon('C:\\Users\\hp\\Desktop\\event\\icon\\camera.png'))
        self.cam.setGeometry(QtCore.QRect(540, 280, 20, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cam.setFont(font)
        self.cam.setStyleSheet("baskground-color: none;")
        self.cam.setObjectName("cam")
        self.pic = QtWidgets.QLabel(self.Loginwidget)
        self.pic.setGeometry(QtCore.QRect(2, 0, 321, 362))
        self.pic.setText("")
        self.pic.setObjectName("pic")
        self.label = QtWidgets.QLabel(self.Loginwidget)
        self.label.setGeometry(QtCore.QRect(330, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Loginwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 40, 81, 31))
        self.label_2.setStyleSheet("background-color: none;")
        self.label_2.setObjectName("label_2")
        self.close = QtWidgets.QPushButton(self.Loginwidget)
        self.close.clicked.connect(exit)
        self.close.setGeometry(QtCore.QRect(574, 10, 12, 12))
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
            loginForm.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.Loginwidget)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(558, 10, 12, 12))
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

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

        self.login.clicked.connect(self.log_in)
        self.cam.clicked.connect(self.cam_recognition)
        
        pixmap = QPixmap("C:\\Users\\hp\\Desktop\\event\\image\\img.jpg")
        pixmap = pixmap.scaled(321, 362, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.pic.setPixmap(pixmap)
        self.pic.setStyleSheet("QLabel { border-radius: 5px; background-color: none; overflow: hidden; }")

        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'registred/'

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image_path in images_paths:
                encoding = self.get_encoding(image_path)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)
                   
    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        return None

    def retranslateUi(self, loginForm):
        _translate = QtCore.QCoreApplication.translate
        loginForm.setWindowTitle(_translate("loginForm", "Form"))
        self.user_name.setPlaceholderText(_translate("loginForm", "Saisie Nom"))
        self.password.setPlaceholderText(_translate("loginForm", "Saisie mots de passe"))
        self.login.setText(_translate("loginForm", "Entrer"))
        self.label.setText(_translate("loginForm", "Saisie Votre Information "))
        self.label_2.setText(_translate("loginForm", "Bonjour,"))

    def log_in(self):
        conn = connection.connection
        cursor = None

        try:
                if not conn.connected: 
                     conn.connect()
                cursor = conn.cursor()

                name = self.user_name.text()
                password = self.password.text()

                if not name and not password:
                      self.erreur()
                
                query = "SELECT nom, photo FROM logevent WHERE nom = ? AND mpass = ? ;"
                cursor.execute(query, (name, password))
                result = cursor.fetchone()

                if result:
                   username = result[0]
                   pic_path = result[1]
                   self.open(username, pic_path)
                else:
                   self.erreur()
        except Exception as e:
            print("Erreur: ", e)
        finally:
                if cursor and not cursor.closed:
                   cursor.close()

    def open(self, username, pic_path):
        from dash import Ui_dash 
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_dash()

        self.work.setupUi(self.work_window)
        self.work.set_user_info(username, pic_path)
        self.work_window.show()
        loginForm.hide()

    def erreur(self):
        from erreur import Ui_erreur
        self.work_window = QtWidgets.QMainWindow()
        self.work = Ui_erreur()

        self.work.setupUi(self.work_window)
        self.work_window.show()
        def close():
             self.work_window.close()
        self.work.pushButton_2.clicked.connect(close)


    def cam_recognition(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if not ret:
            return

        conn = connection.connection
        cursor = conn.cursor()

        try:
            timeout = 5 
            start_time = time.time()
            while time.time() - start_time < timeout:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                faces = face_recognition.face_locations(frame_rgb)
                encodings = face_recognition.face_encodings(frame_rgb, faces)

                encodings_np = np.array(encodings)

                if len(encodings_np) > 0:  
                    for encoding_np in encodings_np:
                        results = face_recognition.compare_faces(self.known_faces, encoding_np)
                        if True in results:
                            index = results.index(True)
                            name = self.known_names[index]

                            query = "SELECT nom, photo FROM logevent WHERE nom = ?;"
                            cursor.execute(query, (name,))
                            result = cursor.fetchone()

                            if result:
                                username = result[0]
                                pic_path = result[1]
                                self.open(username, pic_path)
                                cap.release()  
                                return  
            cap.release()
            print("Délai de détection du visage atteint.")
        except Exception as e:
            print("Erreur: ", e)
        finally:
            if cursor and not cursor.closed:
                cursor.close()
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loginForm = QtWidgets.QWidget()
    ui = Ui_loginForm()
    ui.setupUi(loginForm)
    loginForm.show()
    sys.exit(app.exec_())