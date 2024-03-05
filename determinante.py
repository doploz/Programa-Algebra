def calcular_determinante(matriz):
    n = len(matriz)
    
    # Caso base: si la matriz es 1x1, la determinante es el único elemento
    if n == 1:
        return matriz[0][0]
    
    # Caso base: si la matriz es 2x2, calcular la determinante directamente
    if n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    
    det = 0
    
    # Iterar sobre la primera fila de la matriz para calcular la determinante
    for j in range(n):
        # Calcular el cofactor de la primera fila y columna j
        cofactor = matriz[0][j] * calcular_cofactor(matriz, 0, j)
        # Agregar o restar el cofactor a la determinante según el signo
        det += (-1) ** j * cofactor
    
    return det

def calcular_cofactor(matriz, fila, columna):
    submatriz = []
    n = len(matriz)
    
    # Crear la submatriz eliminando la fila y la columna especificadas
    for i in range(1, n):
        fila_temp = []
        for j in range(n):
            if j != columna:
                fila_temp.append(matriz[i][j])
        submatriz.append(fila_temp)
    
    # Calcular el cofactor recursivamente utilizando la determinante
    return calcular_determinante(submatriz)



