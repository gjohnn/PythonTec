
from functions import es_primo

n = int(input("Ingrese n: "))

print("Es primo!") if es_primo(n) else print("No es primo!")