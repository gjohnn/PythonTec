suma = 0
while True:
    n = -1
    while n <0:
        n = int(input("Ingresar entero positivo: "))
    if n==0:
        break
    suma +=n

print(f"Suma total: {suma}")