while True:
    n = int(input("Ingrese N entero positivo: "))
    if n>0:
        break

for i in range(0,n+1):
    if i%2==1:
        print(f"{i}, ", end="")