"""
Realiza un programa que calcule la potencia, para ello pide por teclado 
la base y el exponente. Pueden ocurrir tres cosas:
El exponente sea positivo, sólo tienes que imprimir la potencia.
El exponente sea 0, el resultado es 1.
El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
"""
print("Programa que calcule la potencia")
base = int(input("Ingresa la base:"))
exp = int(input ("Ingresa el exponente:"))
num = abs(exp)
if exp == 0 :
    print("El resultado de la potencia es: 1")
else:
    if exp > 0:
        print(f"El resultado de la potencia es: {base**exp}")
    else:
        print(f"El resultado de la potencia es: {base**num}") 
print("Fin del programa")