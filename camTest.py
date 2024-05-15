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


class FaceRecognitionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.cap = cv2.VideoCapture(0)

        self.known_faces = []
        self.known_names = []

        self.registered_faces = 'registred/'

        layout = QVBoxLayout(self)
        self.label = QLabel()
        layout.addWidget(self.label)

        for name in os.listdir(self.registered_faces):
            images_mask = os.path.join(self.registered_faces, name, '*.jpg')
            images_paths = glob.glob(images_mask)
            for image_path in images_paths:
                encoding = self.get_encoding(image_path)
                if encoding is not None:
                    self.known_faces.append(encoding)
                    self.known_names.append(name)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

        self.detecteur = dlib.get_frontal_face_detector()
        model_path = "C:\\Users\\hp\\Desktop\\shape_predictor_68_face_landmarks.dat"

        try:
            self.predictor = dlib.shape_predictor(model_path)
        except RuntimeError as e:
            print("erreur: ", e)
            sys.exit(1)

        self.face_detect_time = None
        self.face_leave_time = None
        self.last_detection_day = None

        self.duree = []

    def get_encoding(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        if len(face_encodings) > 0:
            return face_encodings[0]
        return None

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        faces = face_recognition.face_locations(frame_rgb)
        self.point_id(frame_rgb, frame)
        self.time(faces)

        for face in faces:
            top, right, bottom, left = face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            encoding = face_recognition.face_encodings(frame_rgb, [face])[0]

            rslt = face_recognition.compare_faces(self.known_faces, encoding)

            if any(rslt):
                name = self.known_names[rslt.index(True)]
            else:
                name = 'inconnue'

            cv2.putText(frame, name, (left + 20, bottom + 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)


        frame = cv2.resize(frame, (640, 480))
        image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def point_id(self, rgb, frame):
        faces = self.detecteur(rgb)
        for face in faces:
            landmarks = self.predictor(rgb, face)

            for i in range(68):
                x = landmarks.part(i).x
                y = landmarks.part(i).y
                cv2.circle(frame, (x, y), 1, (0, 0, 255), -1)

    def time(self, faces):
        
        if faces:
            if self.face_detect_time is None:
                self.face_detect_time = datetime.now()
                self.last_detection_day = self.face_detect_time.date()
                print("Le temps d'arrivée:", self.face_detect_time.strftime("%H:%M:%S"))
                
        else:
            if self.face_leave_time is None and self.face_detect_time is not None:
                if self.last_detection_day == datetime.now().date():
                    self.face_leave_time = datetime.now()
                    print("Heure de départ:", self.face_leave_time.strftime("%H:%M:%S"))
                    duree_personne = self.face_leave_time - self.face_detect_time
                    self.duree.append(duree_personne)
                    total_seconds = sum(d.total_seconds() for d in self.duree)
                    total_duration = timedelta(seconds=total_seconds)
                    print("Durée:", duree_personne)
                    print("Durée totale:", total_duration)
                    self.face_detect_time = None
                    self.face_leave_time = None

    def closeEvent(self, event):
        self.cap.release()
        event.accept()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = FaceRecognitionWidget()
    window.setWindowTitle("Face Recognition")
    window.show()
    sys.exit(app.exec_())
