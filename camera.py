from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import os
import face_recognition
import glob
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime, timedelta
import sys
import dlib
import connection


class Ui_cam(object):
    def __init__(self) -> None:
        super().__init__()
        self.cap = cv2.VideoCapture(0)
        self.detected_faces = set() 
        self.conn = connection.connection 

        self.widget = QtWidgets.QWidget()  
        self.setupUi(self.widget) 
        
        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'emp/'

        layout = QVBoxLayout()
        self.widget.setLayout(layout)
        layout.addWidget(self.captur)

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image in images_paths:
                encoding = self.get_encoding(image)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)

        self.timer = QTimer()
        self.timer.timeout.connect(self.captur_face)
        self.timer.start(30)

        self.detecteur = dlib.get_frontal_face_detector()
        model_path = "C:\\Users\\hp\\Desktop\\shape_predictor_68_face_landmarks.dat"

        self.predicteur = dlib.shape_predictor(model_path)

        self.face_detect_time = None
        self.face_leave_time = None

        self.arrive = []
        self.depart = []

        self.duree = []
        self.rowPosition = 0

    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        return None
    
    def point_id(self, rgb, frame):
        faces = self.detecteur(rgb)
        for face in faces:
            landmarks = self.predicteur(rgb, face)

            for i in range(68):
                x = landmarks.part(i).x
                y = landmarks.part(i).y
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    def captur_face(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)
        self.point_id(frame_rgb, frame)


        for face in faces:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            encoding = face_recognition.face_encodings(frame_rgb, [face])[0]

            rst = face_recognition.compare_faces(self.known_faces, encoding)

            if any(rst):
                name = self.known_names[rst.index(True)]
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 128, 0), 2)
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 128, 0), 2)
 
                self.time(faces, name)  
                cursor = self.conn.cursor()
                query = "SELECT cin, nom, heurArrive, heurDepart, durre FROM participent WHERE cin = ?"
                cursor.execute(query, (name,))
                result = cursor.fetchall()
                
                self.presence.setRowCount(len(result))


                for row, data in enumerate(result):
                    if data is not None:  
                        cin = data[0]
                        nom = data[1]
                        heurArrive = data[2]
                        heurDepart = data[3]
                        duree = data[4]

                        cin_item = QTableWidgetItem(str(cin))  
                        nom_item = QTableWidgetItem(nom)
                        arrive_item = QTableWidgetItem(str(heurArrive))  
                        depart_item = QTableWidgetItem(str(heurDepart))  
                        duree_item = QTableWidgetItem(str(duree))  

                        self.presence.setItem(row, 0, cin_item)
                        self.presence.setItem(row, 1, nom_item)
                        self.presence.setItem(row, 2, arrive_item)
                        self.presence.setItem(row, 3, depart_item)
                        self.presence.setItem(row, 4, duree_item)

                
            else:
                name = 'inconnue'
                cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
                continue


        frame = cv2.resize(frame, (640, 480))
        image = QtGui.QImage(frame, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(image)
        self.captur.setPixmap(pixmap)

    def time(self, faces, name):
        cursor = self.conn.cursor()

        if faces:
            if self.face_detect_time is None: 
                self.face_detect_time = datetime.now().strftime("%H:%M:%S")
                self.arrive.append(self.face_detect_time)

                arrive = min(self.arrive)
                query = "UPDATE participent SET heurArrive = ? WHERE cin = ?;"
                cursor.execute(query, (arrive, name))
                self.conn.commit()
            else:
                if self.face_leave_time is None and self.face_detect_time is not None:
                    self.face_leave_time = datetime.now().strftime("%H:%M:%S")
                    self.depart.append(self.face_leave_time)
                    depart = max(self.depart)
                    query1 = "UPDATE participent SET heurDepart = ? WHERE cin = ?;"
                    cursor.execute(query1, (depart, name))
                    self.conn.commit()

                    self.face_leave_time = None
                    self.face_detect_time = None

                    arrive = datetime.strptime(min(self.arrive), "%H:%M:%S")
                    depart = datetime.strptime(max(self.depart), "%H:%M:%S")

                    self.duration(arrive, depart, name)

        # today = datetime.now().date()
        # query_update_arrival = """
        # UPDATE participent
        # SET heurArrive = NULL
        # WHERE heurArrive IS NOT NULL
        # AND getdate() != ?;
        # """
        # cursor.execute(query_update_arrival, (today,))
        # self.conn.commit()

    def duration(self, arrive, depart, name):
        cursor = self.conn.cursor()
        duree_personne = depart - arrive

        self.duree.append(duree_personne)
        total = sum(d.total_seconds() for d in self.duree)
        total_duration = timedelta(seconds=total)

        total_duration_str = str(total_duration)

        query2 = "UPDATE participent SET durre = ? WHERE cin = ?;"
        cursor.execute(query2, (total_duration_str, name))
        
        self.conn.commit()

    def list_abs(self):
        cursor = self.conn.cursor()
        query = """SELECT cin, nom
FROM participent
WHERE heurArrive IS NULL;"""
        cursor.execute(query)
        result = cursor.fetchall()

        self.absance.setRowCount(len(result))

        for row, data in enumerate(result):
            cin = data[0]
            nom = data[1]
            
            cin_item = QTableWidgetItem(cin)
            nom_item = QTableWidgetItem(nom)
             
            self.absance.setItem(row, 0, cin_item)
            self.absance.setItem(row, 1, nom_item)
            

    def setupUi(self, cam):
        cam.setObjectName("cam")
        cam.resize(869, 588)
        cam.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        cam.setAttribute(QtCore.Qt.WA_TranslucentBackground)  
        self.widget = QtWidgets.QWidget(cam)
        self.widget.setGeometry(QtCore.QRect(20, 10, 841, 581))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;")
        self.widget.setObjectName("widget")
        def reduit():
            cam.showMinimized()
        self.reduit = QtWidgets.QPushButton(self.widget)
        self.reduit.clicked.connect(reduit)
        self.reduit.setGeometry(QtCore.QRect(806, 10, 12, 12))
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
        self.close = QtWidgets.QPushButton(self.widget)
        self.close.setGeometry(QtCore.QRect(820, 10, 12, 12))
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
        self.captur = QtWidgets.QLabel(self.widget)
        self.captur.setGeometry(QtCore.QRect(120, 20, 591, 301))
        self.captur.setStyleSheet("background-color: rgb(223, 223, 223);")
        self.captur.setText("")
        self.captur.setObjectName("captur")
        self.absance = QtWidgets.QTableWidget(self.widget)
        self.absance.setGeometry(QtCore.QRect(600, 370, 211, 192))
        self.absance.setStyleSheet("QTableWidget{\n"
"background-color: rgb(251, 255, 170);\n"
"}QTableWidget::item{\n"
"    background-color: rgb(255, 229, 125);\n"
"}")
        self.absance.setObjectName("absance")
        self.absance.setColumnCount(2)
        self.absance.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.absance.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.absance.setHorizontalHeaderItem(1, item)
        self.presence = QtWidgets.QTableWidget(self.widget)
        self.presence.setGeometry(QtCore.QRect(30, 370, 511, 192))
        self.presence.setStyleSheet("QTableWidget{\n"
"background-color: rgb(251, 255, 170);\n"
"}QTableWidget::item{\n"
"    background-color: rgb(255, 229, 125);\n"
"}")
        self.presence.setObjectName("presence")
        self.presence.setColumnCount(5)
        self.presence.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.presence.setHorizontalHeaderItem(4, item)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 340, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(610, 340, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(cam)
        QtCore.QMetaObject.connectSlotsByName(cam)

        self.list_abs()

    def retranslateUi(self, cam):
        _translate = QtCore.QCoreApplication.translate
        cam.setWindowTitle(_translate("cam", "cam"))
        item = self.absance.horizontalHeaderItem(0)
        item.setText(_translate("cam", "CIN"))
        item = self.absance.horizontalHeaderItem(1)
        item.setText(_translate("cam", "Nom"))
        item = self.presence.horizontalHeaderItem(0)
        item.setText(_translate("cam", "CIN"))
        item = self.presence.horizontalHeaderItem(1)
        item.setText(_translate("cam", "NOM"))
        item = self.presence.horizontalHeaderItem(2)
        item.setText(_translate("cam", "Heure d arrive"))
        item = self.presence.horizontalHeaderItem(3)
        item.setText(_translate("cam", "Heure de départ"))
        item = self.presence.horizontalHeaderItem(4)
        item.setText(_translate("cam", "Temps de Travail "))
        self.label_2.setText(_translate("cam", "Liset de présence"))
        self.label_3.setText(_translate("cam", "Liset d\'absance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cam = QtWidgets.QWidget()
    ui = Ui_cam()
    ui.setupUi(cam)  
    cam.show()
    sys.exit(app.exec_())
