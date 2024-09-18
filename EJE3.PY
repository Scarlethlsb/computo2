import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Formulario de Información Personal')
        self.setGeometry(100, 100, 400, 250)

       
        self.setStyleSheet("background-color: #f5f5f5;")

        layout = QVBoxLayout()
        layout.setSpacing(15)  

        self.cedula_label = QLabel('Número de DUI:')
        self.cedula_label.setFont(QFont('Arial', 12, QFont.Bold))  
        self.cedula_label.setStyleSheet("color: #333333;") 
        layout.addWidget(self.cedula_label)

        self.cedula_input = QLineEdit()
        self.cedula_input.setPlaceholderText('Ingrese su número de DUI')  
        self.cedula_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")  # estilo de borde y relleno
        layout.addWidget(self.cedula_input)

        self.nombre_label = QLabel('Nombre Completo:')
        self.nombre_label.setFont(QFont('Arial', 12, QFont.Bold))  
        self.nombre_label.setStyleSheet("color: #333333;") 
        layout.addWidget(self.nombre_label)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText('Ingrese su nombre completo')  
        self.nombre_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")  # estilo de borde y relleno
        layout.addWidget(self.nombre_input)

        self.submit_button = QPushButton('Enviar')
        self.submit_button.setFont(QFont('Arial', 12, QFont.Bold)) 
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px;")  # Estilo del botón
        self.submit_button.clicked.connect(self.submit_info)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_info(self):
        cedula = self.cedula_input.text()
        nombre = self.nombre_input.text()

        if not cedula or not nombre:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese tanto el número de cédula como el nombre completo.')
        else:
            QMessageBox.information(self, 'Información Enviada', f'Número de DUI: {cedula}\nNombre Completo: {nombre}')

app = QApplication(sys.argv)
window = PersonalInfoWindow()
window.show()
sys.exit(app.exec_())