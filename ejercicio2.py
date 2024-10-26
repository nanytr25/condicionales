"""
Programa que pida un número y diga si es positivo, negativo o 0.
"""
print("Programa que verifica si un numero es positivo, negativo o 0")
num = int(input("Ingresa un numero: "))
if num == 0:
    print("El numero es 0")
else:
    if num > 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
print("Fin del programa")