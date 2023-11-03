"""Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si
no que los sume."""

n1 = float(input("Ingrese n1: "))
n2 = float(input("Ingrese n2: "))

if n1 == n2:
    print(n1*n2)
elif n1>n2:
    print(n1-n2)
else:
    print(n1+n2)