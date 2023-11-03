password = "nashe"
intentos = 3
for i in range(1,4):
    pass1 = input("Ingrese contraseña: ")
    if password == pass1:
        print("Bienvenido!")
        break
    intentos -= 1
    print("Intentos: ", intentos)