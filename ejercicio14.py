"""
Escribe un programa que pida un número entero entre uno y doce e imprima el 
número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.
"""
print("programa que pide al usuario un numero del 1 al 12 y muestre el mes correspondiente")
mes = int(input("Ingresa un numero: "))
if mes == 1:
    print("El mes correspondiente es: Enero")
elif mes == 2:
    print("El mes correspondiente es: Febrero")
elif mes == 3:
    print("El mes correspondiente es: Marzo")
elif mes == 4:
    print("El mes correspondiente es: Abril")
elif mes == 5:
    print("El mes correspondiente es: Mayo")
elif mes == 6:
    print("El mes correspondiente es: Junio")
elif mes == 7:
    print("El mes correspondiente es: Julio")
elif mes == 8:
    print("El mes correspondiente es: Agosto")
elif mes == 9:
    print("El mes correspondiente es: Septiembre")
elif mes == 10:
    print("El mes correspondiente es: Octubre")
elif mes == 11:
    print("El mes correspondiente es: Noviembre")
elif mes == 12:
    print("El mes correspondiente es: Diciembre")
else:
    print("ERROR!")