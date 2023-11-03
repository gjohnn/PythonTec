from functions import validate_dni

dni = int(input("Ingrese dni: "))
print("Es válido!") if validate_dni(dni) else print("No es válido!")


