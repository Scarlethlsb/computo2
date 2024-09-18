import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class MascotasApp(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Datos de Mascotas")  

        
        self.nombres = []
        self.edades = []
        self.razas = []

     
        layout_principal = QVBoxLayout()

        for i in range(3):
           
            label_titulo = QLabel(f"Mascota {i+1}:")
            label_nombre = QLabel("Nombre:")
            entrada_nombre = QLineEdit()

            label_edad = QLabel("Edad:")
            entrada_edad = QLineEdit()

            label_raza = QLabel("Raza:")
            entrada_raza = QLineEdit()

            layout_principal.addWidget(label_titulo)
            layout_principal.addWidget(label_nombre)
            layout_principal.addWidget(entrada_nombre)
            layout_principal.addWidget(label_edad)
            layout_principal.addWidget(entrada_edad)
            layout_principal.addWidget(label_raza)
            layout_principal.addWidget(entrada_raza)

            
            self.nombres.append(entrada_nombre)
            self.edades.append(entrada_edad)
            self.razas.append(entrada_raza)

      
        boton_mostrar = QPushButton("Mostrar Datos")
        boton_mostrar.clicked.connect(self.mostrar_datos)
        layout_principal.addWidget(boton_mostrar)

        
        self.setLayout(layout_principal)

    def mostrar_datos(self):
        datos = []
        for i in range(3):
            nombre = self.nombres[i].text()
            edad = self.edades[i].text()
            raza = self.razas[i].text()

            if nombre and edad and raza:
                datos.append(f"Mascota {i+1}: Nombre: {nombre}, Edad: {edad}, Raza: {raza}")
            else:
                QMessageBox.warning(self, "Advertencia", "Por favor, ingrese todos los datos para las tres mascotas.")
                return

        
        QMessageBox.information(self, "Datos de las Mascotas", "\n".join(datos))


if __name__ == "__main__":
    app = QApplication(sys.argv)


    ventana = MascotasApp()
    ventana.show()

    
    sys.exit(app.exec_())