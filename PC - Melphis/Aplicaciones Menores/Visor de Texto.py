import tkinter as tk

def read_calculations_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    # Separamos el contenido en bloques por líneas vacías
    return [block.strip() for block in content.split('\n\n') if block.strip()]

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculos de Costos")
        
        self.text_display = tk.Text(root, font=("Helvetica", 16), wrap=tk.WORD)
        self.text_display.pack(expand=True, fill=tk.BOTH)

        # Leer los cálculos desde el archivo
        self.text_lines = read_calculations_from_file('calculos.txt')
        self.index = 0
        self.display_next_text()

    def display_next_text(self):
        if self.index < len(self.text_lines):
            self.text_display.delete(1.0, tk.END)  # Borra el contenido anterior
            self.text_display.insert(tk.END, self.text_lines[self.index])  # Inserta el nuevo texto
            self.index += 1
            self.root.after(5000, self.display_next_text)  # Espera 5 segundos antes de mostrar el siguiente

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
