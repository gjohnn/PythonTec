n = 0
cifra = 0
suma = 0

while n<100 or n >999:
    n = int(input("Ingrese n: "))
while n!=0:
    cifra = n%10
    suma += cifra
    n = int(n/10)
print("Suma de los digitos: ", int(suma))