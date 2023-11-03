ammount = 0
while True:
    price = int(input("Ingrese n: "))
    if (price <= 0):
        break
    ammount+=price
print(" ---------------- ")
if ammount>= 1000:
    print(f"Monto: {ammount}")
    print("Descuento del %10!")
    print(f"Monto final: {ammount*0.90}")
else:
    print(f"Monto final: {ammount}")
