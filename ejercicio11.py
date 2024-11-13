"""
La política de cobro de una compañía telefónica es: cuando se realiza una 
llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros 
cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos,
los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos.
Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno
de mañana, 15 %, y en turno de tarde, 10 %. 
Realice un programa para determinar cuánto debe pagar por cada concepto 
una persona que realiza una llamada.
"""
print("Programa que muestre el costo de tu llamada")
t = int(input("¿Cuanto duro la llamada en minutos?:"))
dia = input("¿Que dia se realizo la llamada?:")
turno = ""
if dia != "domingo" : 
    turno = input("¿En que turno se realizo la tamada?:")
if t<= 5:
    costo = (t * 1)
elif t <= 8:
    costo = (5 * 1) + (t - 5) * 0.8
else:
    costo = (5 * 1) + (3 * 0.8) + (2 * 0.7) + (t - 10 ) * 0.5
if dia == "domingo":
    impuesto = (costo * 0.03)
else:
    if turno == "mañana":
        impuesto = (costo * 0.15)
    elif turno =="tarde" :
        impuesto = (costo * 0.10)
costo_total = costo + impuesto
print(f"El costo de la llamada es: {costo_total} ")
