ammount = 0
while True:
    price = int(input("Ingrese n: "))
    if (price <= 0):
        break
    ammount+=price
print(f"Monto final: ${ammount}")