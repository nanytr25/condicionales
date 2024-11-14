"""
 Juego Piedra Papel y Tijera
 Programa que lea las opciones de 2 jugadores, y muestra el resultado
 Empate, gana jugador 1 o gana jugador 2
 Si introducimos una opción que no coindica con piedra, papel o tijera
 Diga que opción Incorrecta
"""
print("Piedra papel o tijera")
j1 = input("Ingresa la opcion del jugador 1:")
j2 = input("Ingresa la opcion del jugador 2:")
if j1 == "piedra" and j2 == "piedra":
    print("Empate")
elif j1 == "papel" and j2 == "papel":
    print("Empate")
elif j1 == "tijeras" and j2 == "tijeras":
    print("Empate")
elif j1 == "papel" and j2 == "piedra":
    print("Gana el jugador 1")
elif j1 == "piedra" and j2 == "papel":
    print("Gana el jugador 2")
elif j1 == "tijeras" and  j2 == "papel":
    print("Gana el jugador 1")
elif j1 == "papel" and j2 == "tijeras":
    print("Gana el jugador 2")
elif j1 == "tijeras" and  j2 == "piedra":
    print("Gana el jugador 2")
elif j1 == "piedra" and j2 == "tijeras":
    print("Gana el jugador 1")
else:
    print("Opcion incorrecta")
