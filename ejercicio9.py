"""
Programa que pida tres números y los muestre ordenados (de mayor a menor);
"""
print("Programa que ordene 3 numeros de mayor a menor")
n1 = int(input("Ingresa el primer numero:"))
n2 = int(input("Ingresa el segundo numero:"))
n3 = int(input("Ingresa el tercer numero:"))
if n1>n2 and n2>3:
    print("", n1, "-", n2, "-",n3)

elif n2>n1 and n1>3:
    print("",n2,"-", n1, "-",n3)

elif n3>n1 and n1>2:
    print("",n3,"-", n1, "-",n2)

elif n3>n2 and n2>1:
    print("",n3,"-", n2, "-",n1)

elif n1>n3 and n3>2:
    print("",n1,"-", n3, "-",n2)

elif n2>n3 and n3>1:
    print("",n2,"-", n3, "-",n1)   
    
else:
    print("Error") 