import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QPushButton, QVBoxLayout, QMessageBox, QLineEdit



#Este programa es una pequeña aplicación de entrada de datos donde el 
# usuario puede ingresar su nombre, seleccionar su género y elegir su edad. 
# Los componentes principales son un campo de texto, un QComboBox para el género, 
# un QSpinBox para la edad y un botón para mostrar los datos ingresados.

#Desglose del programa
# inicialización de la ventana:
# Se define la clase DatosUsuarioApp, que hereda de QWidget, 
# lo que permite crear una ventana gráfica. Dentro de esta clase,
# se configura la interfaz de usuario.


class DatosUsuarioApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Datos del Usuario")

        layout_principal = QVBoxLayout()

        self.nombre_label = QLabel("Nombre:")
        self.nombre_input = QLineEdit()
        layout_principal.addWidget(self.nombre_label)
        layout_principal.addWidget(self.nombre_input)
        
        # Se coloca una etiqueta (QLabel) 
        # que indica al usuario que debe ingresar su nombre en un campo de texto (QLineEdit).

        self.genero_label = QLabel("Género:")
        self.genero_combo = QComboBox()
        self.genero_combo.addItems(["Seleccionar", "Masculino", "Femenino", "No binario", "Otro"])
        layout_principal.addWidget(self.genero_label)
        layout_principal.addWidget(self.genero_combo)
        
        # Aquí se utiliza un QComboBox para proporcionar una lista desplegable de géneros. 
        # El usuario debe seleccionar su género entre las opciones proporcionadas. 
        # La primera opción es “Seleccionar”, que se utiliza como un valor predeterminado vacío.

        self.edad_label = QLabel("Edad:")
        self.edad_spinbox = QSpinBox()
        self.edad_spinbox.setRange(1, 120)  # Rango de 1 a 120 años
        layout_principal.addWidget(self.edad_label)
        layout_principal.addWidget(self.edad_spinbox)
        
        # La edad se selecciona mediante un QSpinBox, que permite al usuario elegir un valor 
        # numérico. El rango de edad permitido es de 1 a 120 años, lo que cubre una variedad 
        # común de edades.

        self.boton_mostrar = QPushButton("Mostrar Datos")
        self.boton_mostrar.clicked.connect(self.mostrar_datos)
        layout_principal.addWidget(self.boton_mostrar)
        
        #Se añade un botón que, al hacer clic, llama al método mostrar_datos.
        # Este método recoge los datos ingresados por el usuario, los valida y 
        # los muestra en una ventana emergente.

        self.setLayout(layout_principal)

    def mostrar_datos(self):
        nombre = self.nombre_input.text()
        genero = self.genero_combo.currentText()
        edad = self.edad_spinbox.value()

        if not nombre:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingrese su nombre.")
            return

        if genero == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Por favor, seleccione su género.")
            return

        datos = f"Nombre: {nombre}\nGénero: {genero}\nEdad: {edad} años"
        QMessageBox.information(self, "Datos del Usuario", datos)

#El método mostrar_datos realiza las siguientes acciones:

# Valida que el nombre y género hayan sido seleccionados. 
# Si alguno está vacío o si el género no ha sido seleccionado, muestra un mensaje de advertencia.
# Muestra los datos ingresados en un cuadro de diálogo QMessageBox si todos los campos están 
# completos.

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = DatosUsuarioApp()
    ventana.show()
    sys.exit(app.exec_())


#Este programa es útil en situaciones donde se requiere recopilar información básica de un
# usuario (nombre, género y edad) de manera eficiente. 
# Es un ejemplo típico de formulario simple y adaptable a distintas aplicaciones, 
# como registros, encuestas o validaciones de perfiles en aplicaciones más grandes.