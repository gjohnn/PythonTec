n = None
qty_pares = 0
while True:
    n = int(input("Ingrese n: "))
    if (n <= -1):
        break
    aux = n
    suma = 0
    cifra = 0
    while aux != 0:
        cifra = aux%10
        suma+= cifra
        aux =int(aux/10)
    print(suma)
