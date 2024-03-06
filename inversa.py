from matriz import *
def calcular_inversa(matriz):
    # Función para calcular el determinante
    def calcular_determinante(matriz):
        n = len(matriz)
        
        if n == 1:
            return matriz[0][0]
        
        if n == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        
        det = 0
        
        for j in range(n):
            cofactor = matriz[0][j] * calcular_cofactor(matriz, 0, j)
            det += (-1) ** j * cofactor
        
        return det
    
    # Función para calcular el cofactor
    def calcular_cofactor(matriz, fila, columna):
        submatriz = []
        n = len(matriz)
        
        for i in range(1, n):
            fila_temp = []
            for j in range(n):
                if j != columna:
                    fila_temp.append(matriz[i][j])
            submatriz.append(fila_temp)
        
        return calcular_determinante(submatriz)
    
    # Obtener la dimensión de la matriz
    n = len(matriz)
    
    # Calcular el determinante de la matriz
    det = calcular_determinante(matriz)
    
    # Verificar si la matriz es cuadrada y su determinante es distinto de cero (para tener inversa)
    if n != len(matriz[0]) or det == 0:
        print("La matriz no es invertible.")
        return None
    
    # Inicializar la matriz de cofactores
    cofactores = []
    for i in range(n):
        fila_temp = []
        for j in range(n):
            cofactor = (-1) ** (i + j) * calcular_cofactor(matriz, i, j)
            fila_temp.append(cofactor)
        cofactores.append(fila_temp)
    
    # Calcular la adjunta (transpuesta de la matriz de cofactores)
    adjunta = [[cofactores[j][i] for j in range(n)] for i in range(n)]
    
    # Calcular la inversa multiplicando la adjunta por 1/det
    inversa = [[round(adjunta[i][j] / det, 2) for j in range(n)] for i in range(n)]
    
    return inversa

