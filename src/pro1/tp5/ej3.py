from functions import define_user, validate_dni

name_1 = input("Ingrese nombre: ")
name_2 = input("Ingrese segundo nombre: ")
surname = input("Ingrese apellido: ")

dni = 0
while validate_dni(dni) == False:
    dni = int(input("Ingrese dni: "))

print(define_user(name_1,name_2,surname,dni))

