n = None
contador_primo = 0
while True:
    es_primo = True
    n = int(input("Ingrese n (0 para salir):"))
    if n == 0:
        break
    
    while n<0:
        n = int(input("Ingrese n (mayor a 0):"))
        
    for i in range(2, n):
        if n % i == 0:
            es_primo = False
            break
    if es_primo == True:
        contador_primo+=1

print(f"Cantidad de N° primos: {contador_primo}")