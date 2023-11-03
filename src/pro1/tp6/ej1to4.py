numbers = []

while True:
    n = int(input("Ingrese número (0 para salir): "))
    if n==0 :
        break
    numbers.append(n)
    print(numbers)

n_to_delete = int(input("Ingrese número a eliminar: "))

for i in range(0,len(numbers)-1):
    if numbers[i] == n_to_delete:
        numbers.pop(i)
        break
print(numbers)

summatory_numbers = 0

for e in numbers:
    summatory_numbers+=e
print(f"Suma de los números del array: {summatory_numbers}")


n_limit = int(input("Ingresa un número límite: "))
new_numbers = [e for e in numbers if e <= n_limit]

# Imprimir la nueva lista
print("Elementos menores que el número límite:")
for e in new_numbers:
    print(e)

