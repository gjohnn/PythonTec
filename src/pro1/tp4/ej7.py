numbers = []

for n in range(1, 101):
    numbers.append(n)


find_number = int(input("Ingrese número a encontrar: "))

for i in numbers:
    if i == find_number:
        print("Encontrado!")
        break