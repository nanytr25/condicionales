"""
Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
el dí­a correspondiente. 
Si introducimos otro número nos da un error.
"""
print("Programa que prida un numero del 1 al 7 y muestre el dia correspondiente")
dia = int(input("Ingresa un numero:"))
if dia == 1 :
    print("El dia correspondiente es: Lunes")
elif dia == 2 :
    print("El dia correspondiente es: Martes")
elif dia == 3 :
    print("El dia correspondiente es: Miercoles")
elif dia == 4 :
    print("El dia correspondiente es: Jueves")
elif dia == 5 :
    print("El dia correspondiente es: Viernes")
elif dia == 6 :
    print("El dia correspondiente es: Sabado")
elif dia == 7 :
    print("El dia correspondiente es: Domingo")
else:
    print("ERROR!")