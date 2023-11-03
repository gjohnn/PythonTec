from functions import min_and_max

numbers = []
while True:
    n = int(input("Ingrese n (0 para salir): "))
    if n == 0:
        break
    numbers.append(n)

min_and_max(numbers)
