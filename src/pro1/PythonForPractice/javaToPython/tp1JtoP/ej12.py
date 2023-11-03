n = int(input("Ingrese día: "))

while n<1 or n>7:
    n = int(input("Ingrese día: "))

if n==6 or n==7:
    print("Dia NO laboral!")
else:
    print("Dia laboral!")