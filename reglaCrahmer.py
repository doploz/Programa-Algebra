def determinant(matrix):
    # Función para calcular la determinante de una matriz cuadrada
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            minor = [row[:j] + row[j+1:] for row in matrix[1:]]
            det += (-1) ** j * matrix[0][j] * determinant(minor)
        return det

def cramer_rule(coefficients, constants):
    # Función para aplicar la regla de Cramer
    n = len(coefficients)
    det_coefficients = determinant(coefficients)
    
    if det_coefficients == 0:
        return "El sistema no tiene solución única (determinante de coeficientes igual a cero)"
    
    results = []
    for i in range(n):
        modified_coefficients = [row[:] for row in coefficients]
        for j in range(n):
            modified_coefficients[j][i] = constants[j]
        det_modified = determinant(modified_coefficients)
        results.append(det_modified / det_coefficients)
    
    return results

# Ejemplo de uso:
coefficients = [[2, -1, 3],
                [1, 2, 1],
                [1, 1, -1]]
constants = [7, 8, 0]

print("Resultado usando la regla de Cramer:", cramer_rule(coefficients, constants))
