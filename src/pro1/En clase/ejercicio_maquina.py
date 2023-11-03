print("------------- Cajero automático -------------")
n = 1
money = 10000
while n != 0:
    print("-- MENU --")
    print("1) Extraer dinero")
    print("2) Ingresar dinero")
    n = int(input("Que desea hacer? (ingrese 0 para salir): "))
    if n == 1:
        extract_money = float(input("Ingrese monto a extraer: "))
        while extract_money > money:
            print("Excede el dinero disponible en su cuenta")
            extract_money = float(input("Ingrese monto a extraer: "))
        money -= extract_money
        print(f"Extrajo ${extract_money}")
        print(f"Dinero disponible: {money}")
    elif n==2:
        put_money = float(input("Ingrese dinero: "))
        money+=put_money
        print(f"Dinero disponible: {money}")