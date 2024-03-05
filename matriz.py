import tkinter as tk

def ingresar_datos():
    for i in range(tamaño):
        for j in range(tamaño):
            valor = entry_grid[i][j].get()
            matriz[i][j] = int(valor)
    imprimir_matriz()

def imprimir_matriz():
    texto_matriz.delete(1.0, tk.END)  # Limpiar el texto anterior
    for fila in matriz:
        texto_matriz.insert(tk.END, " ".join(map(str, fila)) + "\n")

def crear_interfaz():
    global tamaño
    tamaño = int(entry_tamaño.get())

    ventana_grafica.destroy()  # Cerrar la ventana de ingreso de tamaño

    global root
    root = tk.Tk()
    root.title("Matriz Resultante")

    global matriz
    matriz = [[0 for _ in range(tamaño)] for _ in range(tamaño)]

    global entry_grid
    entry_grid = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            entry = tk.Entry(root, width=5)
            entry.grid(row=i, column=j)
            fila.append(entry)
        entry_grid.append(fila)

    btn_ingresar = tk.Button(root, text="Ingresar Datos", command=ingresar_datos)
    btn_ingresar.grid(row=tamaño, columnspan=tamaño)

    global texto_matriz
    texto_matriz = tk.Text(root, height=tamaño, width=2*tamaño)
    texto_matriz.grid(row=tamaño+1, columnspan=tamaño)

ventana_grafica = tk.Tk()
ventana_grafica.title("Ingreso de Datos en Matriz")

label_tamaño = tk.Label(ventana_grafica, text="Ingrese el tamaño de la matriz cuadrada:")
label_tamaño.grid(row=0, column=0)

entry_tamaño = tk.Entry(ventana_grafica)
entry_tamaño.grid(row=0, column=1)

btn_crear = tk.Button(ventana_grafica, text="Crear Matriz", command=crear_interfaz)
btn_crear.grid(row=1, columnspan=2)

ventana_grafica.mainloop()
