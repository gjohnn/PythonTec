# Solicitar al usuario un número entero
n = int(input("Ingrese un número entero: "))

# Verificar si el número es primo
es_primo = True  # Suponemos que el número es primo

if n <= 1:
    es_primo = False
else:
    for i in range(2, n):
        #Comprobar si es divisible por numeros entre 1 y n
        #Si lo es no es primo
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")