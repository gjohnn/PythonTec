while True:
    # Inicializar variables de conteo para cada vocal
    qty_a = 0
    qty_e = 0
    qty_i = 0
    qty_o = 0
    qty_u = 0
    word = input(f"Ingrese palabra: ").lower()
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
    validate_repeat = input("Repetir juego? (s/n) : ").lower()
    if validate_repeat == "n":
        break
