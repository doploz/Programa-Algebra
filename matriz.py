def crear_matriz(tamaño):
    matriz = []
    for _ in range(tamaño):
        fila = []
        for _ in range(tamaño):
            fila.append(0)  # Inicializamos todos los elementos a 0
        matriz.append(fila)
    return matriz

def ingresar_datos(matriz):
    tamaño = len(matriz)
    for i in range(tamaño):
        for j in range(tamaño):
            while True:
                try:
                    valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
                    matriz[i][j] = valor
                    break  # Sale del bucle while si se ingresó un valor numérico válido
                except ValueError:
                    print("Por favor, ingrese un valor numérico.")

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def crear_constantes(tamaño):
    constantes = []
    for i in range(tamaño):
        while True:
            try:
                valor = int(input(f"Ingrese el valor de la constante para la ecuación {i+1}: "))
                constantes.append(valor)
                break  # Sale del bucle while si se ingresó un valor numérico válido
            except ValueError:
                print("Por favor, ingrese un valor numérico para la constante.")
    return constantes

def crear_Matriz(tamaño):
    
    matriz = crear_matriz(tamaño)
    print("Ingrese los datos de la matriz:")
    ingresar_datos(matriz)
    print("La matriz resultante es:")
    imprimir_matriz(matriz)
    return matriz

def crear_SistemaLineal(tamaño):
    
    constantes = crear_constantes(tamaño)
    return  constantes

"""
matriz, constantes = crear_Matriz()
print("Constantes del sistema:", constantes)
"""