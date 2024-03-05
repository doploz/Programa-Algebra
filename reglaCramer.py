from determinante import *
from matriz import *

def resolver_sistema_lineal(coeficientes, constantes):
    """
    Resuelve un sistema de ecuaciones lineales utilizando la regla de Cramer.
    """
    n = len(coeficientes)
    det_A = calcular_determinante(coeficientes)
    
    if det_A == 0:
        return "El sistema no tiene solución única."
    
    soluciones = []
    for i in range(n):
        # Crear una copia de la matriz de coeficientes y reemplazar la columna i con las constantes
        matriz_temporal = [fila[:] for fila in coeficientes]
        for j in range(n):
            matriz_temporal[j][i] = constantes[j]
        
        # Calcular el determinante de la matriz temporal y la solución para la variable i
        det_temporal = calcular_determinante(matriz_temporal)
        solucion = det_temporal / det_A
        soluciones.append(solucion)
    
    return soluciones

