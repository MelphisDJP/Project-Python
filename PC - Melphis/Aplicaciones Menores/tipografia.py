import fontforge
import os

# Ruta a la carpeta donde tienes los archivos SVG
ruta_svg = r'C:\Users\MELGRAPH01\Downloads\Caracteres'

# Abre una nueva fuente en FontForge
fuente = fontforge.font()

# Lista de caracteres en el mismo orden que los archivos SVG
# Los primeros son letras mayúsculas, luego letras minúsculas, números y símbolos
caracteres = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    '=', '>', '<', 'π', 'Δ'
]

# Iterar sobre los archivos SVG y asignarles un carácter de la lista
for i, nombre_caracter in enumerate(caracteres, start=1):
    archivo_svg = f"Caracter-{i:02}.svg"  # Formato de nombre del archivo
    ruta_archivo = os.path.join(ruta_svg, archivo_svg)
    
    if os.path.exists(ruta_archivo):
        glifo = fuente.createChar(ord(nombre_caracter), nombre_caracter)  # Crear el glifo con el código unicode
        glifo.importOutlines(ruta_archivo)  # Importar el archivo SVG en el glifo
        print(f'Importado {archivo_svg} como {nombre_caracter}')
    else:
        print(f'El archivo {archivo_svg} no existe en la ruta especificada')

# Guardar la fuente en formato .ttf o .otf
fuente.generate('C:/Users/MELGRAPH01/Project-Python/PC - Melphis/Practica 1 Microeconomía/Practica 1 Microeconomía/MiFuente.ttf')

print("Fuente generada exitosamente.")
