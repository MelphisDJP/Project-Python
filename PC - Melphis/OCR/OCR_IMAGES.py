import sys
import pytesseract
from PIL import ImageGrab
import numpy as np
import cv2
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QTextEdit, QMessageBox, 
                             QHBoxLayout, QCheckBox, QLabel, 
                             QScrollArea)

# Configura la ruta de tesseract en tu sistema si es necesario
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Ajusta la ruta

class OCRApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.history = []  # Lista para almacenar el historial de transcripciones
        self.last_text = ""  # Variable para almacenar el último texto extraído

    def initUI(self):
        self.setWindowTitle('OCR App')
        layout = QVBoxLayout()

        self.startButton = QPushButton('Start OCR')
        self.startButton.clicked.connect(self.run_ocr)
        layout.addWidget(self.startButton)

        self.highlightCheckbox = QCheckBox("Extraer solo texto resaltado")
        layout.addWidget(self.highlightCheckbox)

        # Área de texto para mostrar el último texto extraído
        self.lastTextEdit = QTextEdit()
        self.lastTextEdit.setReadOnly(True)
        layout.addWidget(self.lastTextEdit)

        # Botón para copiar el último texto extraído
        self.copyButton = QPushButton('Copy Last Text')
        self.copyButton.clicked.connect(self.copy_last_text)
        layout.addWidget(self.copyButton)

        # Botón para mostrar el historial
        self.showHistoryButton = QPushButton('Mostrar Historial')
        self.showHistoryButton.clicked.connect(self.show_history_window)
        layout.addWidget(self.showHistoryButton)

        self.setLayout(layout)
        self.resize(400, 300)

    def run_ocr(self):
        try:
            print("Intentando capturar imagen del portapapeles...")
            image = ImageGrab.grabclipboard()

            if image is None:
                print("No hay imagen en el portapapeles.")
                QMessageBox.warning(self, "Advertencia", "No hay imagen en el portapapeles.")
                return

            print("Imagen capturada. Procesando...")

            # Verificar el modo de la imagen
            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Convertir la imagen a formato OpenCV
            open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            if self.highlightCheckbox.isChecked():
                # Si se selecciona la opción de resaltar, extraer texto del área resaltada
                text = self.extract_highlighted_text(open_cv_image)
            else:
                # Preprocesamiento de la imagen
                gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
                _, thresh_image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY)

                # Convertir la imagen a texto usando Tesseract
                custom_config = r'--oem 3 --psm 6'  # Puedes ajustar los parámetros según sea necesario
                text = pytesseract.image_to_string(thresh_image, config=custom_config)

            print("Texto extraído:", text)
            self.last_text = text.strip()
            self.lastTextEdit.setPlainText(self.last_text)
            self.history.append(self.last_text)
            if len(self.history) > 10:
                self.history.pop(0)

        except Exception as e:
            print(f"Error durante el OCR: {str(e)}")
            QMessageBox.critical(self, "Error", str(e))



    def extract_highlighted_text(self, image):
        # Convertir a espacio de color HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Definir el rango de color amarillo para la detección
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        # Crear una máscara para el color amarillo
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        # Aplicar la máscara a la imagen original
        highlighted_image = cv2.bitwise_and(image, image, mask=mask)

        # Convertir la imagen resaltada a texto
        text = pytesseract.image_to_string(highlighted_image)

        return text

    def copy_last_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.last_text)
        QMessageBox.information(self, "Copiar", "Texto del último OCR copiado al portapapeles.")

    def show_history_window(self):
        history_window = HistoryWindow(self.history)
        history_window.show()  # Usar show() en lugar de exec_

class HistoryWindow(QWidget):
    def __init__(self, history):
        super().__init__()
        self.history = history
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Historial de Transcripciones')
        layout = QVBoxLayout()

        # Área de scroll para el historial
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaLayout = QVBoxLayout()
        self.scrollAreaContent.setLayout(self.scrollAreaLayout)
        self.scrollArea.setWidget(self.scrollAreaContent)
        layout.addWidget(self.scrollArea)

        self.populate_history()

        self.setLayout(layout)
        self.resize(400, 300)

    def populate_history(self):
        # Limpiar el contenido anterior
        for i in reversed(range(self.scrollAreaLayout.count())): 
            widget = self.scrollAreaLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for i, entry in enumerate(self.history):
            short_text = (entry[:300] + '...') if len(entry) > 300 else entry
            
            # Crear un layout para cada entrada
            entryLayout = QHBoxLayout()

            # Mostrar texto corto
            textLabel = QLabel(short_text)
            entryLayout.addWidget(textLabel)

            # Botón para copiar
            copyButton = QPushButton('Copy')
            copyButton.clicked.connect(lambda _, text=entry: self.copy_to_clipboard(text))
            entryLayout.addWidget(copyButton)

            # Botón para eliminar
            deleteButton = QPushButton('Delete')
            deleteButton.clicked.connect(lambda _, index=i: self.delete_entry(index))
            entryLayout.addWidget(deleteButton)

            self.scrollAreaLayout.addLayout(entryLayout)

    def copy_to_clipboard(self, text):
        clipboard = QApplication.clipboard()
        clipboard.setText(text)
        QMessageBox.information(self, "Copiar", "Texto copiado al portapapeles.")

    def delete_entry(self, index):
        if 0 <= index < len(self.history):
            self.history.pop(index)
            self.populate_history()  # Actualizar la visualización del historial

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ocrApp = OCRApp()
    ocrApp.show()
    sys.exit(app.exec_())