import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class PersonalInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Información Personal')
        self.setGeometry(100, 100, 400, 200)

        # Fondo de la ventana
        self.setStyleSheet("background-color: #f0f0f0;")  

        layout = QVBoxLayout()
        layout.setSpacing(20)  

        self.name_label = QLabel('Nombre Completo: Oscar Ulises Ortiz Cruz')
        self.name_label.setAlignment(Qt.AlignCenter)  
        self.name_label.setFont(QFont('Arial', 16, QFont.Bold))  
        self.name_label.setStyleSheet("color: #2e8b57;")  
        layout.addWidget(self.name_label)

        self.age_label = QLabel('Edad: 20 años')
        self.age_label.setAlignment(Qt.AlignLeft) 
        self.age_label.setFont(QFont('Verdana', 14, QFont.StyleItalic)) 

        self.age_label.setStyleSheet("color: #ff6347;") 

        layout.addWidget(self.age_label)

    
        self.setLayout(layout)
 
app = QApplication(sys.argv)
window = PersonalInfoWindow()
window.show()
sys.exit(app.exec_())
