def validate_dni(dni):
    if len(str(dni)) > 8 or len(str(dni)) < 7:
        return False
    return True


def validate_len_string(word):
    # Borrar espacios del principio y del final del string
    word = word.strip()
    # Crear array con las palabras en orden y separadas
    words = word.split()
    # Mostrar longitud de la ultima palabra si es que existe
    if words:
        return len(words[-1])
    else:
        return 0


def define_user(name_1, name_2, surname, dni):
    print(f"Nombre: {name_1.title()} {name_2.title()} {surname.title()}")
    print(f"DNI: {dni}")
    dni = str(dni)
    user_id = name_1.title() + str(len(surname)) + dni[:3]
    print(f"ID: {user_id}")


def validate_multiple(n1, n2):
    if n1 % n2 == 0:
        print(f"N1( {n1} ) es multiplo de N2( {n2} )")
    elif n2 % n1 == 0:
        print(f"N2( {n2} ) es multiplo de N1( {n1} )")
    else:
        print("No tienen relación!")


def temp_average(temp_max, temp_min):
    return (temp_max + temp_min) / 2


def separate_letter(word):
    new_word = ""
    for e in word:
        if e != " ":
            new_word += e + " "
    return new_word


def min_and_max(arr):
    min_n = 0
    max_n = 0
    for e in arr:
        if e > max_n:
            max_n = e
        elif min_n > e:
            min_n = e
    print(f"Mayor: {max_n}")
    print(f"Menor: {min_n}")


import math


def circumference(radio):
    perimeter = 2 * radio * math.pi
    area = math.pi * (radio**2)
    print(f"Perímetro: {perimeter}")
    print(f"Área: {area}")


def login(user):
    name = user["name"]
    password = user["password"]

    if name != "usuario1" or password != "asdasd":
        print("Datos incorrectos!")
        return False
    return True


def discount(cart, discounts):
    precio_total = 0

    for producto, precio in cart.items():
        if producto in discounts:
            precio_con_descuento = precio * (1 - discounts[producto] / 100)
            precio_total += precio_con_descuento
        else:
            precio_total += precio

    return precio_total


# ej 11
def own_function_1(function_2, arr):
    res = []
    for e in arr:
        res.append(function_2(e))
    return res


def sumar_cinco(x):
    return x + 5


def word_dictionary(word):
    letters = {}
    i = 1
    for e in word:
        letters.setdefault(i, e)
        i += 1
    return letters


def module_vector(vector):
    module_calc = 0
    for e in vector:
        module_calc += e**2
    module_calc = math.sqrt(module_calc)
    return module_calc


def es_primo(x):
    validate_primo = True
    for i in range(2, x):
        if x % i == 0:
            validate_primo = False
    return validate_primo


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def compare_digits(n, d):
    qty_digit = 0
    while n != 0:
        digit = n % 10
        if digit == d:
            qty_digit += 1
        n //= 10
    return qty_digit


def summatory_digits(n):
    sum_digits = 0
    while n != 0:
        digit = n % 10
        sum_digits += digit
        n //= 10
    return sum_digits
