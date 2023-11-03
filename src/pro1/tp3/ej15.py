while True:
    n = int(input("Ingrese N entero positivo: "))
    if n>0:
        break
    
for i in range(1,n+1):
    if n%i==0:
        print(f"{i} es divisor de {n}")