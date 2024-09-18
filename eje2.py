import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QFont

class SecretKeyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Entrada de Clave Secreta')
        self.setGeometry(100, 100, 300, 150)

        self.setStyleSheet("background-color: #f7f7f7;")  

        layout = QVBoxLayout()
        layout.setSpacing(15) 

        self.instruction_label = QLabel('Ingrese su clave secreta:')
        self.instruction_label.setFont(QFont('Arial', 14, QFont.Bold)) 
        self.instruction_label.setStyleSheet("color: #333333;")  
        layout.addWidget(self.instruction_label)

       
        self.secret_key_input = QLineEdit()
        self.secret_key_input.setEchoMode(QLineEdit.Password)  
        self.secret_key_input.setPlaceholderText('Ingrese su clave aquí')  
        self.secret_key_input.setStyleSheet("border: 1px solid #cccccc; border-radius: 5px; padding: 5px;")  # Estilo de borde y relleno
        layout.addWidget(self.secret_key_input)

    
        self.submit_button = QPushButton('Enviar')
        self.submit_button.setFont(QFont('Arial', 12, QFont.Bold)) 
        self.submit_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; border-radius: 5px; padding: 10px;")  # estilo del botón
        self.submit_button.clicked.connect(self.submit_secret_key)
        layout.addWidget(self.submit_button)

        
        self.setLayout(layout)

    def submit_secret_key(self):
       
        secret_key = self.secret_key_input.text()

        
        if not secret_key:
            QMessageBox.warning(self, 'Error', 'Por favor, ingrese una clave secreta.')
        else:
            QMessageBox.information(self, 'Clave Secreta', f'La clave ingresada es: {secret_key}')


app = QApplication(sys.argv)
window = SecretKeyWindow()
window.show()
sys.exit(app.exec_())