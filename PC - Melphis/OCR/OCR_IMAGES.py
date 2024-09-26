import pytesseract
from PIL import ImageGrab
import numpy as np

# Configura la ruta de tesseract en tu sistema si es necesario
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Descomenta y ajusta la ruta

# Función principal para realizar OCR en la imagen del portapapeles
def ocr_from_clipboard():
    try:
        # Captura la imagen del portapapeles
        image = ImageGrab.grabclipboard()

        if image is None:
            print("No hay imagen en el portapapeles.")
            return
        
        # Convertir la imagen a un formato que pytesseract pueda usar
        text = pytesseract.image_to_string(image)

        # Imprimir el texto extraído
        print("Texto extraído del portapapeles:")
        print(text)

    except Exception as e:
        print(f"Error: {e}")

# Ejecutar la función
if __name__ == "__main__":
    ocr_from_clipboard()
