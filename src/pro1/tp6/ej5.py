numbers = []

while True:
    n = int(input("Ingrese número (0 para salir): "))
    if n == 0:
        break
    numbers.append(n)
    print(numbers)

for i in range(0, len(numbers) - 1):
    index = 0
    

qty_foreach_number = []
for e in numbers:
    count = numbers.count(e)
    if (e, count) in qty_foreach_number:
        continue
    tuple_num = (e,count)
    qty_foreach_number.append(tuple_num)

print(qty_foreach_number)
