n = 1
qty_pares = 0
while True:
    n = int(input("Ingrese n: "))
    if (n <= -1):
        break
    if n%2 == 0:
        qty_pares+=1
    aux = n
    suma = 0
    cifra = 0
    while aux != 0:
        cifra = aux%10
        suma+= cifra
        aux =int(aux/10)
    print(suma)
print(f"Cantidad de N° pares: {qty_pares}")