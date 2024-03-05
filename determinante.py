import numpy as np
import tkinter as tk
from tkinter import messagebox

def calcular_determinante():
    try:
        n = int(entry_tamano.get())
        matriz = []
        for i in range(n):
            fila = []
            for j in range(n):
                fila.append(float(entries_matriz[i][j].get()))
            matriz.append(fila)

        matriz = np.array(matriz)
        determinante = np.linalg.det(matriz)
        messagebox.showinfo("Resultado", f"La determinante de la matriz es: {determinante}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos para los elementos de la matriz.")
    except np.linalg.LinAlgError:
        messagebox.showerror("Error", "La matriz no es cuadrada. Por favor ingrese una matriz cuadrada.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Determinante")

# Crear y posicionar los elementos de la interfaz
label_tamano = tk.Label(root, text="Tamaño de la matriz cuadrada:")
label_tamano.grid(row=0, column=0)

entry_tamano = tk.Entry(root)
entry_tamano.grid(row=0, column=1)

button_calcular = tk.Button(root, text="Calcular Determinante", command=calcular_determinante)
button_calcular.grid(row=0, column=2)

label_matriz = tk.Label(root, text="Ingrese los elementos de la matriz:")
label_matriz.grid(row=1, column=0, columnspan=3)

entries_matriz = []
for i in range(3):
    fila_entries = []
    for j in range(3):
        entry = tk.Entry(root)
        entry.grid(row=i+2, column=j)
        fila_entries.append(entry)
    entries_matriz.append(fila_entries)

# Ejecutar la aplicación
root.mainloop()
