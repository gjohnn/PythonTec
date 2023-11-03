from functions import factorial

read_numbers = 0
while True:
    n = int(input("Ingrese n (n menor a 0 para salir): "))
    if n < 0:
        break
    fact_n = factorial(n)
    read_numbers += 1
    print(f"El factorial de {n}: {fact_n}")

print("Numeros leídos:", read_numbers)