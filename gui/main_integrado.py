import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QWidget, QGridLayout, QMessageBox, QFileDialog
)
from PySide2.QtGui import QPixmap, QImage
from PySide2.QtCore import Qt
#import motor_control
from motores import motor_control
from procesamiento.reconstruccion import reconstruir_desde_archivo
import cv2
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Captura Holográfica")
        self.setGeometry(100, 100, 1000, 700)

        motor_control.inicializar_gpio()

        self.image_label_capturada = QLabel("Imagen Capturada")
        self.image_label_capturada.setAlignment(Qt.AlignCenter)
        self.image_label_capturada.setStyleSheet("border: 2px solid #999; background-color: #f9f9f9;")
        self.image_label_capturada.setFixedSize(450, 300)

        self.image_label_reconstruida = QLabel("Imagen Reconstruida")
        self.image_label_reconstruida.setAlignment(Qt.AlignCenter)
        self.image_label_reconstruida.setStyleSheet("border: 2px solid #999; background-color: #f9f9f9;")
        self.image_label_reconstruida.setFixedSize(450, 300)

        images_layout = QHBoxLayout()
        images_layout.addWidget(self.image_label_capturada)
        images_layout.addWidget(self.image_label_reconstruida)

        self.capture_button = QPushButton("Cargar Imagen y Reconstruir")
        self.capture_button.clicked.connect(self.abrir_y_procesar_imagen)

        self.open_chamber_button = QPushButton("Abrir Recámara")
        self.open_chamber_button.clicked.connect(self.abrir_recamara)

        self.close_chamber_button = QPushButton("Cerrar Recámara")
        self.close_chamber_button.clicked.connect(self.cerrar_recamara)

        recamara_buttons_layout = QHBoxLayout()
        recamara_buttons_layout.addWidget(self.open_chamber_button)
        recamara_buttons_layout.addWidget(self.close_chamber_button)

        action_buttons_layout = QVBoxLayout()
        action_buttons_layout.addWidget(self.capture_button)
        action_buttons_layout.addLayout(recamara_buttons_layout)

        self.controls_grid = QGridLayout()
        self.btn_up = QPushButton("↑")
        self.btn_left = QPushButton("←")
        self.btn_right = QPushButton("→")
        self.btn_down = QPushButton("↓")

        self.btn_up.clicked.connect(motor_control.mover_arriba)
        self.btn_down.clicked.connect(motor_control.mover_abajo)
        self.btn_left.clicked.connect(motor_control.mover_izquierda)
        self.btn_right.clicked.connect(motor_control.mover_derecha)

        self.controls_grid.addWidget(self.btn_up, 0, 1)
        self.controls_grid.addWidget(self.btn_left, 1, 0)
        self.controls_grid.addWidget(self.btn_right, 1, 2)
        self.controls_grid.addWidget(self.btn_down, 2, 1)

        main_layout = QVBoxLayout()
        main_layout.addLayout(images_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(action_buttons_layout)
        main_layout.addSpacing(20)
        main_layout.addLayout(self.controls_grid)
        main_layout.setContentsMargins(20, 20, 20, 20)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def abrir_y_procesar_imagen(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Imágenes (*.png *.jpg *.bmp)")
        if not ruta:
            return

        self.mostrar_imagen(self.image_label_capturada, ruta)

        # Ejecutar reconstrucción
        img_reconstruida = reconstruir_desde_archivo(ruta)
        if img_reconstruida is not None:
            self.mostrar_np_imagen(self.image_label_reconstruida, img_reconstruida)

    def mostrar_imagen(self, label, ruta):
        pixmap = QPixmap(ruta)
        if not pixmap.isNull():
            label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio))
        else:
            self.mostrar_mensaje("Error", "No se pudo cargar la imagen.")

    def mostrar_np_imagen(self, label, array):
        height, width = array.shape
        qimg = QImage(array.data, width, height, width, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimg)
        label.setPixmap(pixmap.scaled(label.size(), Qt.KeepAspectRatio))

    def abrir_recamara(self):
        self.mostrar_mensaje("Recámara", "¡Recámara abierta!")

    def cerrar_recamara(self):
        self.mostrar_mensaje("Recámara", "¡Recámara cerrada!")

    def mostrar_mensaje(self, titulo, mensaje):
        popup = QMessageBox(self)
        popup.setWindowTitle(titulo)
        popup.setText(mensaje)
        popup.setIcon(QMessageBox.Information)
        popup.setStandardButtons(QMessageBox.Ok)
        popup.exec_()

    def closeEvent(self, event):
        motor_control.limpiar_gpio()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec_())