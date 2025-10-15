#pip install pyside2
#pip install opencv-python

import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QWidget, QGridLayout, QMessageBox, QFrame
)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt
from motores import motor_control

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Captura Holográfica")
        self.setGeometry(100, 100, 1000, 700)

        # Inicializar motores
        motor_control.inicializar_gpio()

        # ======= Área de imágenes =======
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

        # ======= Botones principales =======
        self.capture_button = QPushButton("Capturar Imagen")
        self.capture_button.clicked.connect(self.simular_captura)

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

        # ======= Botones de movimiento (↑ ← → ↓) =======
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

        # ======= Layout principal =======
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

    # ======= Métodos funcionales =======
    def simular_captura(self):
        pixmap_capturada = QPixmap("assets/img_test.jpg")
        if pixmap_capturada.isNull():
            self.mostrar_mensaje("Error", "No se encontró la imagen capturada.")
        else:
            self.image_label_capturada.setPixmap(pixmap_capturada.scaled(
                self.image_label_capturada.width(),
                self.image_label_capturada.height(),
                Qt.KeepAspectRatio
            ))

        # Simular reconstrucción también
        pixmap_reconstruida = QPixmap("assets/img_test.jpg")  # Aquí podrías usar otra imagen procesada
        if not pixmap_reconstruida.isNull():
            self.image_label_reconstruida.setPixmap(pixmap_reconstruida.scaled(
                self.image_label_reconstruida.width(),
                self.image_label_reconstruida.height(),
                Qt.KeepAspectRatio
            ))

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
