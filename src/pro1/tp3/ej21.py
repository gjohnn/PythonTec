highest_number = 0
while True:
    n = int(input("Ingrese n: "))
    if n == 0:
        break
    if n>highest_number:
        highest_number = n

print(f"Número más alto: {highest_number}")