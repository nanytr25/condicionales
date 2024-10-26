"""
ondicionales: if
    Evaluan expresiones boleanas

Estructuras:

   if expresion:
       instrucciones
   if expresion:
       instrucciones
   else:
       instrucciones
   if expresion:
       instrucciones
   elif expresion:
       instrucciones
   else:
       instrucciones                
"""
print("Programa que verifica si un numero es positivo")
num = int(input("Ingresa un numero: "))
# preguntar el numero es mayor a 0:
if num > 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")

print("programa que verifica si un numero es par o impar")
num = int(input("Ingresa un numero: "))
if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es inpar")    
print("Fin del programa") 
