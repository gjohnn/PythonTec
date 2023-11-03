from functions import module_vector
n1 = int(input("Ingrese punto A del vector: "))
n2 = int(input("Ingrese punto B del vector: "))

vector = (n1,n2)

vector = module_vector(vector)

print(f"Módulo del vector: {vector}")

