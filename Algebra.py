from reglaCrahmer import*

def input_matrix():
    # Función para ingresar una matriz desde el usuario
    matrix = []
    while True:
        try:
            row = list(map(float, input("Ingrese una fila de la matriz separada por espacios: ").split()))
            matrix.append(row)
        except ValueError:
            print("Ingrese números válidos.")
        else:
            if len(row) != len(matrix[0]):
                print("Las filas deben tener la misma cantidad de elementos.")
            else:
                break
    return matrix

def input_constants(n):
    # Función para ingresar los términos constantes de un sistema de ecuaciones lineales
    constants = []
    for i in range(n):
        while True:
            try:
                constant = float(input(f"Ingrese el término constante para la ecuación {i+1}: "))
            except ValueError:
                print("Ingrese un número válido.")
            else:
                constants.append(constant)
                break
    return constants

def main():
    while True:
        print("\n1. Calcular determinante de una matriz")
        print("2. Calcular regla de Cramer")
        print("3. Salir")
        choice = input("Ingrese su elección: ")
        
        if choice == "1":
            print("Ingrese la matriz:")
            matrix = input_matrix()
            print("Determinante de la matriz:", determinant(matrix))
        elif choice == "2":
            n = int(input("Ingrese el número de ecuaciones en el sistema: "))
            print("Ingrese los coeficientes de la matriz de coeficientes:")
            coefficients = input_matrix()
            print("Ingrese los términos constantes:")
            constants = input_constants(n)
            print("Resultado usando la regla de Cramer:", cramer_rule(coefficients, constants))
        elif choice == "3":
            break
        else:
            print("Opción inválida. Por favor, elija nuevamente.")

if __name__ == "__main__":
    main()
