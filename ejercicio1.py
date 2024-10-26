"""
Programa que pida dos números e indique Cuál es el mayor
Si los dos son iguales que muestre el mensaje "Son iguales"

"""
print("Programa que pida dos números e indique Cuál es el mayor")
num = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa el segundo numero:"))
if num == num2 :
    print("Los numeros son iguales")
else:
    if num > num2:
        print(f"El numero mayor es: {num}")
    else:
        print(f"El numero mayor es: {num2}") 
print("Fin del programa")