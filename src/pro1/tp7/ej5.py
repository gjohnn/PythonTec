#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de 
#números en orden descendente en lugar de ascendente.
from functions import bubble_sort

new_list = [4, 5, 6, 3, 2, 1, 6, 88, 55, 33, 12, 34, 75, 2, 1, 7, 0]

bubble_sort(new_list)
print(new_list)
new_list.reverse()
print(new_list)