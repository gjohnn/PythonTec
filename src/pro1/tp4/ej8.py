while True:
    option = 14
    while option < 0 or option >3:
        print("1) OPCION")
        print("2) OPCION")
        print("3) OPCION")
        print("0) SALIR")

        option = int(input("Ingrese opción: "))
    if option==0:
        break
    elif option==1:
        print(" ----------- Mensaje 1")
    elif option==2:
        print(" ----------- Mensaje 2")
    elif option==3:
        print(" ----------- Mensaje 3")