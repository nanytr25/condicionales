"""
Realiza un programa que pida por teclado el resultado (dato entero) obtenido 
al lanzar un dado de seis caras y muestre por pantalla el número en letras 
(dato cadena) de la cara opuesta al resultado obtenido.
* Nota 1: En las caras opuestas de un dado de seis caras están los números: 
1-6, 2-5 y 3-4.
* Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, 
se mostrará el mensaje: "ERROR: número incorrecto.".
"""
print("Programa que muestra el numero opuesto en letras de una cara de un dado")
cara = int(input("Ingresa la cara dada al lanzar el dado:"))
if cara == 1 :
    print("La cara opuesta en letras es: Seis")
elif cara == 6 :
    print("La cara opuesta en letras es: Uno")
elif cara == 2 :
    print("La cara opuesta en letras es: Cinco")
elif cara == 5 :
    print("La cara opuesta en letras es: Dos")
elif cara == 3 :
    print("La cara opuesta en letras es: Cuatro")
elif cara == 4 :
    print("La cara opuesta en letras es: Tres")
else:
        print("ERROR: número incorrecto.")
   