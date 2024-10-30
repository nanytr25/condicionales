"""
 Escribe un programa que pida un nombre de usuario y una contraseña 
 y si se ha introducido "pepe" y "asdasd" se indica "Has entrado al sistema", 
 sino se da un error.
"""
user = input("Ingresa tu nombre de usuario:")
passw = input("Ingresa la contraseña:")
if user == "Nany" and passw == "nanytr" :
    print("Has ingresado al sistema!")
else: 
    print("Usuario o Contraseña incorrectos!")
print("Fin del programa")