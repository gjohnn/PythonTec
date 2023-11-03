# EJ1 - los que están escritos son los que están incorrectos
print("-------------------- EJ1 --------------------")

print("b | empieza con un número")
print("c | correcto pero con mala práctica")
print("d | empieza con un carácter")
print("e | utiliza buenas practicas pero utiliza tilde y virgulilla ")
print("f | palabra reservada")
print("g | empieza con un carácter")
print("k | utiliza un operador")
print("L | utiliza un carácter no valido")
print("m | empieza con un número")
print("n | palabra reservada")
print("o | utiliza un operador")
print("p | empieza con caracter no valido")
print("r | válido pero mala práctica ")
print("t | es recomendado evitar el uso de virgulilla")
print("v | contiene caracter no valido")
print("w | empieza con número")
print("x | contiene caracter no valido")

print("-------------------- EJ2 --------------------")

print("a | x = 30")
print("c | x = 25")
print("d | x = 8")
print("e | x = 13")
print("f | x = 8")

print("-------------------- EJ3 --------------------")

print("a | float")
print("b | float")
print("c | int")
print("d | int ")
print("e | string")
print("f | string")
print("g | string")
print("h | int")
print("i | int")
print("j | float")
print("k | float")
print("l | string")
print("m | boolean")
print("n | boolean")
print("o | boolean")

print("-------------------- EJ4 --------------------")

print("c | NO VALIDA")
print("d | NO VALIDA")
print("e | NO VALIDA")
print("i | NO VALIDA")
print("j | NO VALIDA")
print("k | NO VALIDA")
print("l | NO VALIDA")

print("-------------------- EJ5 --------------------")

var_int = 1
print(type(var_int), " Valor: ", var_int)
var_float = 1.5
print(type(var_float), " Valor: ", var_float)
var_complex = complex(5 + 2j)
print(type(var_complex), " Valor: ", var_complex)
var_string = "Juan Guerrero"
print(type(var_string), " Valor: ", var_string)
var_bool = 3 < 2
print(type(var_bool), " Valor: ", var_bool)
var_list = [1, 2]
print(type(var_list), " Valor: ", var_list)
var_tuple = (1, 2)
print(type(var_tuple), " Valor: ", var_tuple)
var_dict = {1: 23}
print(type(var_dict), " Valor: ", var_dict)
var_null = None
print(type(var_null), " Valor: ", var_null)

print("-------------------- EJ6 --------------------")

frase = "Caminante, no hay camino, se hace camino al andar."
print("a | ", frase[5])
print("b | ", frase[-1])
print("c | ", frase[0:8])
print("d | ", frase[::3])

print("-------------------- EJ7 --------------------")

print("Inversa:", frase[::-1])
print("Obtener 'hace':", frase[29 : 29 + 4])

print("-------------------- EJ8 --------------------")

var_ej8_1 = "lucas mauricio barros"
var_ej8_2 = "El qUe No arRiesGa, nO gANa."
print(var_ej8_1.title())
print(var_ej8_2.lower())
print(var_ej8_2.upper())

print("-------------------- EJ9 --------------------")
print("Se utiliza ** para potencia")
print("b/2)-4*a*c")  # A
print("(3*a*b)-5*a+12*a-17")  # B
print("b+d)/(c+4)")  # C
print("(a*b)/b+2)")  # D
print("1/b + 3*a/c + 1")  # E
print("1/(b+3)+a/b+1")  # F
print("a**2 + b**2")  # G
print("a+b)**2")  # H
print("b**(1/3)+34")  # I
print("a/b)*(c+d)* 3.14")  # J
print("a+b)/(u+(d/b))")  # K

print("-------------------- EJ10 (EN EL WORD) --------------------")

print("-------------------- EJ11 --------------------")

a = 5
b = 2
c = 6
x = -6
y = 4
var_ej11 = a + b * (5 - c / 2) + (7 - x) / (y + 4)
print("Resultado de a+b*(5-c/2)+(7-x)/(y+4):", var_ej11)

print("-------------------- EJ12 --------------------")
# a
print("a | 5+3: ", 5 + 3)
# b
print("b | Promedio de 4+7+9:", (4 + 7 + 9) / 3)
# c
rectangulo_base = 8
rectangulo_alt = 5
print("c | Area del rectangulo (base: 8, alt:5):", rectangulo_base * rectangulo_alt)
# d
es_par = 3
if es_par % 2 == 0:
    print("d | Es par")
else:
    print("d | No es par")
# e
print("e | Doble de 16:", 16 * 2)
# f
print("f | 6 veces la diferencia entre 8 y 3:", (8 - 3) * 6)
# g
print("g | 2*6 - 4+3: ", (2 * 6) - (4 + 3))
# h
n_multiplo = 9
if n_multiplo % 3 == 0:
    print("h | Multiplo de 2 o 3: de 3")
elif n_multiplo % 2 == 0:
    print("h | Multiplo de 2 o 3: de 2")
else:
    print("h | Multiplo de 2 o 3: de ninguno")
# i
n_precio = 13
if n_precio >= 15 and n_precio <= 90:
    print("i | El precio está entre 15 y 90")
elif n_precio < 15:
    print("i | El precio es menor a 15")
elif n_precio > 90:
    print("i | El precio es mayor a 90")
# j hasta m
n_entero = 10
print("j | +12:", n_entero + 12)
print("k | -5:", n_entero - 5)
print("l | x3:", n_entero * 3)
print("m | /2:", n_entero / 2)

print("-------------------- EJ13 --------------------")

print("False")  # A
print("True")  # B
print("False")  # C
print("False")  # D
print("False")  # E
print("True")  # F
print("True")  # G
print("True")  # H
print("True")  # I

print("-------------------- EJ14 --------------------")

x = 5
x += 1
print(f"c | {x}")
x = 5
x -= 2
print("b |", x)
x = 5
x *= 5
print("c |", x)
x = 5
x /= 5
print("d |", x)

print("-------------------- EJ15 --------------------")

print("a | colores[3] = 'amarrilo'")
print("b | colores[0] = 'rojo' --- colores[8] = 'rosa")
lista_numeros = ["tres", "dos", "cinco", "cuatro", "uno"]
print("c |", lista_numeros)
print("d | colores[2] = 'verde'")
numeros = (10, 1, 5, 11)
n_deseado = numeros[0] + numeros[2] + numeros[3] - numeros[1]
print(
    "e | Llegar a 25 con tupla (10,1,5,11): numeros[0]+numeros[2]+numeros[3]-numeros[1] =",
    n_deseado,
)
print("f | Tiene 4 elementos")
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
print("g | diccionario['c'] =", diccionario["c"])

print("-------------------- EJ16 --------------------")

nombre = input("Ingresa tu nombre (EJEMPLO): ")
print(f"¡Hola, {nombre}! Bienvenido/a")
print("--- A ---")

n1 = int(input("Ingresa n1: "))
n2 = int(input("Ingresa n2: "))
print("Suma:",n1+n2)

print("--- B ---")

edad = int(input("Ingrese edad: "))
print(f"Le falta {100-edad} años para llegar a los 100 años")

print("-------------------- EJ17 --------------------")

numero_par_impar = 8
es_par_impar = print("a | Es par") if numero_par_impar%2==0 else print("a | Es impar")

n_input = int(input("b | Ingrese n: "))
n_absoluto = print("Absoluto:",n_input) if (n_input>=0) else print("Absoluto:", -n_input)

n1 = int(input("Ingresar n1: "))
n2 = int(input("Ingresar n2: "))

es_mayor = print(n1, "es mayor que",n2) if n1>n2 else print(n2, "es mayor que",n1)