from functions import compare_digits

while True:
    n = int(input("Ingrese n (0 para salir): "))
    if n == 0:
        break
    digit = int(input("Ingrese digito: "))
    print(f"Cantidad de veces que aparece el digito en el número: {compare_digits(n,digit)}")