
from functions import factorial, es_primo, summatory_digits,compare_digits

highest_n = 0
while True:
    n = int(input("Ingrese número primo: "))
    if es_primo(n) == False:
        break
    if highest_n < n:
        highest_n =n
    print(f"Suma de sus dígitos: {summatory_digits(n)}")
    digit = int(input("Ingrese digito: "))
    print(f"Cantidad de veces que aparece el digito en el número: {compare_digits(n,digit)}")
    print(" --------------------------------------------------------- ")

print(f"Factorial de {highest_n} (número más alto): {factorial(highest_n)}")