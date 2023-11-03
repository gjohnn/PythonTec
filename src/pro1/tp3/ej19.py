qty_objective = float(input("Introduzca cantidad de dinero que desea ahorrar: "))

money_saving = 0

while money_saving < qty_objective:
    print(f"Cantidad de dinero en alcancía: {money_saving}")
    money_input = float(input("Ingresar dinero: "))
    money_saving+=money_input

print("Se alcanzó el ahorro deseado!")