num = float(input("Ingrese dinero total: "))
print(num)

denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05]
nombres = ["Billetes de 200", "Billetes de 100", "Billetes de 50", "Billetes de 20", "Billetes de 10", "Billetes de 5", "Billetes de 2", "Billetes de 1", "Monedas de 0.50", "Monedas de 0.25", "Monedas de 0.10", "Monedas de 0.05"]

for i in range(len(denominaciones)):
    cantidad = 0
    while num >= denominaciones[i]:
        num -= denominaciones[i]
        cantidad += 1
    print(f"{nombres[i]}: {cantidad}")
