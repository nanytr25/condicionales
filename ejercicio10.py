"""
El director de una escuela está organizando un viaje de estudios, y requiere 
determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
viajes por el servicio. La forma de cobrar es la siguiente: 
si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, 
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
sin importar el número de alumnos. 
Realice un programa que permita determinar el pago a la compañía de autobuses 
y lo que debe pagar cada alumno por el viaje.
"""
print("Programa que calcule el precio de el viaje")
alu = int(input("Cuantos alumnos asistiran al viaje:"))
if alu >= 100:
    print(f"El costo a pagar a la compañia es de:{alu * 65} Euros")
    print("La cooperacion por cada alumno sera de:65 Euros")

elif alu > 50 and alu < 99:
    print(f"El costo a pagar a la compañia es de:{alu * 70} Euros")
    print("La cooperacion por cada alumno sera de:70 Euros")

elif alu > 30 and alu < 49:
    print(f"El costo a pagar a la compañia es de:{alu * 95} Euros")
    print("La cooperacion por cada alumno sera de:95 Euros")

else:
    print("El costo a pagar a la compañia es de: 4000 Euros")
    print(f"La cooperacion por cada alumno sera de:{400 / alu} Euros")