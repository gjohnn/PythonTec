import math

from functions import potency


base = int(input("Ingrese base: "))
n = int(input("Ingrese n a corroborar: "))
if potency(base, n):
    print(f"{n} es una potencia de {base}")
else:
    print(f"{n} no es una potencia de {base}")
