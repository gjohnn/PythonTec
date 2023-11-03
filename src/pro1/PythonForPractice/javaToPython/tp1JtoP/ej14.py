import random
n = int(input("Ingrese n: "))
intentos = 1
aleatorio = random.randint(1,100)
while n!=aleatorio:
    if n<aleatorio:
        print("Es más alto!")
    else:
        print("Es más bajo")
    n = int(input("Ingrese n: "))
    intentos += 1
print("Lo encontraste! | Intentos: ", intentos)