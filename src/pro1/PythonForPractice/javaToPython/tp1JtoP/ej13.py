n = int(input("Ingrese n: "))
contador = 0
for i in range(1,n+1):
    if(n%i == 0):
        contador += 1
    if contador > 2:
        break
if contador==2:
    print("Es primo!")
else:
    print("No es primo")