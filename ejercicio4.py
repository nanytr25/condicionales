"""
Crea un programa que pida al usuario dos números y muestre su división 
si el segundo no es cero, o un mensaje de aviso en caso contrario.
"""
print("Programa que realiza la division de dos numeros")
num = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num2 == 0:
    print("No se puede realizar la division!")
else:
    division = num / num2
    print("El resultado de la division es:", division)
    
print("Fin del programa")