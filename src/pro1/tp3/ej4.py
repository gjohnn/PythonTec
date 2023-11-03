while True:
    n = int(input("Ingrese N entero positivo: "))
    if n>0:
        break

for i in range(n,0,-1):
    print(f"{i}, ",end="")