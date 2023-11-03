qty_n = int(input("Cuantos números desea ingresar? :"))
negative_counter = 0
for i in range(1,qty_n+1):
    n = int(input(f"Ingrese n{i}:"))
    if n <0:
        negative_counter+=1

print(f"Cantidad de números negativos: {negative_counter}")