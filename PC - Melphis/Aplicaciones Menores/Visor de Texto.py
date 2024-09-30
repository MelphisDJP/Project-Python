import tkinter as tk
import os

def read_calculations_from_file(filename):
    full_path = r'C:\Users\Adm\Project-Python\PC - Melphis\Aplicaciones Menores\calculos.txt'
    if not os.path.exists(full_path):
        print(f"Error: El archivo {full_path} no fue encontrado.")
        return []

    # Abrir el archivo con codificación UTF-8
    with open(full_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Separar el contenido por líneas
    return content.splitlines()

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos de Costos")
        
        self.text_display = tk.Text(root, font=("Helvetica", 16), wrap=tk.WORD)
        self.text_display.pack(expand=True, fill=tk.BOTH)

        # Leer los cálculos desde el archivo
        self.text_lines = read_calculations_from_file('calculos.txt')
        self.index = 0

        # Frame para los botones
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botón "Anterior"
        self.previous_button = tk.Button(button_frame, text="◀ Anterior", command=self.display_previous_text)
        self.previous_button.pack(side=tk.LEFT, padx=10)

        # Botón "Siguiente"
        self.next_button = tk.Button(button_frame, text="Siguiente ▶", command=self.display_next_text)
        self.next_button.pack(side=tk.LEFT, padx=10)

        # Mostrar el primer texto
        self.display_next_text()

    def display_next_text(self):
        if self.index < len(self.text_lines):
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, self.text_lines[self.index])  # Inserta el nuevo texto
            self.index += 1
        else:
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, "No hay más cálculos.")  # Mensaje cuando se termine el texto

    def display_previous_text(self):
        if self.index > 0:
            self.index -= 1  # Disminuye el índice
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, self.text_lines[self.index])  # Inserta el texto anterior
        else:
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, "No hay cálculos anteriores.")  # Mensaje si no hay más anteriores

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
