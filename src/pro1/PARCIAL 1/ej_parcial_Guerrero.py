while True:
    name = input("Ingrese nombre: ").title()
    # Validar que el usuario no ingrese String vacio
    if name != "":
        break
    print("Ingrese su nombre!")
#Saludo :D
print(f"Bienvenido/a, {name} :D")

while True:
    # Inicio
    print("--- MENÚ ---")
    print("1) Juego de números")
    print("2) Juego de palabras")
    option = int(input(f"Elija un juego, {name}: "))
    if option == 1 or option == 2:
        break
    print("Ingrese juego correcto!")

if option == 1:
    print("Juego de números!")
    # Mostrar promedio de numeros impares y mostrar el mayor de los numeros pares
    while True:
        # Cantidad de impares
        qty_odd = 0
        # Suma de impares
        sum_of_odd = 0
        # Par más alto
        high_even = 0
        while True:
            number = int(input(f"Ingrese números enteros, {name} (0 para salir): "))
            if number == 0:
                break
            if number % 2 == 0:
                # Corroboro si number es mayor a high_even y asi reemplazarlo
                if number > high_even:
                    high_even = number
            else:
                # Sumo 1 a qty_odd cuando detecte que no es par number
                qty_odd += 1
                # sum_of_odd se va a ir sumando con number
                sum_of_odd += number
        print(f"Mayor número par: {high_even}")
        print(
            f"Promedio de números impares: {sum_of_odd/qty_odd}"
        ) if qty_odd > 0 else print("No hubo numeros impares , Juan")
        # Validar repetir juego
        validate_repeat = input("Juan, repetir juego? (s/n) : ").lower()
        if validate_repeat == "n":
            break
elif option == 2:
    # Contar cantidad de vocales de una frase
    print("Juego de palabras")
    while True:
        # Inicializar variables de conteo para cada vocal
        qty_a = 0
        qty_e = 0
        qty_i = 0
        qty_o = 0
        qty_u = 0
        word = input(f"Ingrese palabra, {name}: ").lower()
        for i in range(0, len(word)):
            letter = word[i]
            # Condiciones para detectar las vocales por cada letra el string word
            if letter == "a":
                qty_a += 1
            elif letter == "e":
                qty_e += 1
            elif letter == "i":
                qty_i += 1
            elif letter == "o":
                qty_o += 1
            elif letter == "u":
                qty_u += 1
        # Mostrar cantidades de vocales
        print(f"Cantidad de 'a': {qty_a}")
        print(f"Cantidad de 'e': {qty_e}")
        print(f"Cantidad de 'i': {qty_i}")
        print(f"Cantidad de 'o': {qty_o}")
        print(f"Cantidad de 'u': {qty_u}")
        # Validar repetir juego
        validate_repeat = input("Juan, repetir juego? (s/n) : ").lower()
        if validate_repeat == "n":
            break
