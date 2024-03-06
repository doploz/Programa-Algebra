from matriz import crear_Matriz
from determinante import *
from reglaCramer import *
from inversa import*

def main():
    opcion = 0
    opdt =0
    opcr = 0
    opin = 0
    while opcion != 4:
        print("-"*34)
        print("-"*10 +"MENÚ PRINCIPAL"+"-"*10)
        print("-"*34)
        print("1. Calcular determinante")
        print("2. Calculadora Regla de Cramer")
        print("3. Calcular la Inversa")
        print("4. Salir")
        try:
            opcion = int(input("Digite su opcion: "))
        except ValueError:
            print("Por favor ingrese solo números.")
            continue
        
        match opcion:
            case 1:
                while opdt != 2:
                    print("-"*32)
                    print("-"*10+"DETERMINANTE"+"-"*10)
                    print("-"*32)
                    try:
                        tama1 = int(input("Ingrese el tamaño de la matriz cuadrada: "))
                    except ValueError:
                        print("Ingresar datos validos")
                        continue
                        
                    matriz = crear_Matriz(tama1)
                    det_matriz = calcular_determinante(matriz)
                    print(f"La determinante de la matriz es: {det_matriz:.2f}")
                    print ("1.Seguir\n2.Salir")
                    
                    try:
                        opdt = int(input("Digite su opción: "))
                    except ValueError:
                        print("Por favor, ingrese un valor válido.")
                        continue
                    
                
                
            case 2:
                while opcr != 2:
                    print("-"*35)
                    print("-"*10+"REGLA DE CRAMER"+"-"*10)
                    print("-"*35)
                    try:
                        tama = int(input("Ingrese el numero de incognitas: ")) 
                    except ValueError:
                        print("")
                        continue
                                    
                    coeficientes = crear_Matriz(tama)
                    constantes = crear_SistemaLineal(tama)
                        
                    soluciones = resolver_sistema_lineal(coeficientes, constantes)
                    print("Soluciones del sistema:", soluciones)
                    
                    print ("1.Seguir\n2.Salir")
                    
                    try:
                        opcr = int(input("Digite su opción: "))
                    except ValueError:
                        print("Por favor, ingrese un número válido.")
                        continue  
            
            case 3:
                
                while opin != 2:
                    print("-"*27)
                    print("-"*10+"INVERSA"+"-"*10)
                    print("-"*27)
                    try:
                        tama2 = int(input("Ingrese el tamaño de la matriz cuadrada: "))
                    except ValueError:
                        print("Ingresar datos validos")
                        continue
                        
                    matriz = crear_Matriz(tama2)
                    inversa = calcular_inversa(matriz)
                    if inversa:
                        print("La inversa de la matriz es:")
                        for fila in inversa:
                            print(fila)
                            
                    print ("1.Seguir\n2.Salir")
                    
                    try:
                        opin = int(input("Digite su opción: "))
                    except ValueError:
                        print("Por favor, ingrese un valor válido.")
                        continue   
                    
            case 4:
                print("¡Gracias por usar el Programa!")    
                break 
            
            case _:
                print("Ingrese un valor válido")
                
