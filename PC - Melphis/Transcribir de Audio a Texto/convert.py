import pyttsx3
import pydub
from pydub import AudioSegment

# Define la ruta al archivo de texto
archivo = 'transcription.txt'

# Define el archivo de salida en formato MP3
archivo_salida = 'salida.mp3'

# Inicializa el motor de Text-to-Speech
engine = pyttsx3.init()

# Lee el contenido del archivo
with open(archivo, 'r', encoding='utf-8') as file:
    contenido = file.read()

# Configura la velocidad de la voz (opcional)
engine.setProperty('rate', 150)  # Ajusta la velocidad de lectura

# Configura el volumen (opcional)
engine.setProperty('volume', 1)  # Ajusta el volumen

# Guarda el texto como un archivo de audio WAV temporal
archivo_temp = 'temp.wav'
engine.save_to_file(contenido, archivo_temp)

# Espera a que se termine de guardar el archivo
engine.runAndWait()

# Convierte el archivo WAV a MP3 usando pydub
audio = AudioSegment.from_wav(archivo_temp)
audio.export(archivo_salida, format='mp3')

print(f'Archivo de audio guardado como {archivo_salida}')
