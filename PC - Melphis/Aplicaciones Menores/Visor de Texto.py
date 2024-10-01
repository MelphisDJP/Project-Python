import tkinter as tk

class App:
    def __init__(self, root, file_path):
        self.root = root
        self.root.title("Cálculos de Costos - Archivo")
        
        # Crear área para mostrar los resultados
        self.text_display = tk.Text(root, font=("Helvetica", 16), wrap=tk.WORD)
        self.text_display.pack(expand=True, fill=tk.BOTH)

        # Leer el contenido del archivo y dividir en líneas con codificación UTF-8
        with open(file_path, 'r', encoding='utf-8') as file:
            self.text_lines = file.read().splitlines()

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

        # Mostrar la primera línea
        self.display_next_text()

    def display_next_text(self):
        """Muestra la siguiente línea de texto."""
        if self.index < len(self.text_lines):
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, self.text_lines[self.index])  # Inserta la nueva línea
            self.index += 1
        else:
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, "No hay más cálculos.")  # Mensaje cuando se termine el texto

    def display_previous_text(self):
        """Muestra la línea anterior de texto."""
        if self.index > 0:  # Evitar índice negativo
            self.index -= 1
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, self.text_lines[self.index])  # Inserta la línea anterior
        else:
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, "No hay cálculos anteriores.")  # Mensaje si no hay más anteriores

if __name__ == "__main__":
    # Especificar la ruta del archivo
    file_path = r'C:\Users\Adm\Project-Python\PC - Melphis\Aplicaciones Menores\calculos.txt'  # Cambia esto a la ruta de tu archivo

    # Crear la ventana de la aplicación
    root = tk.Tk()
    app = App(root, file_path)
    root.mainloop()
