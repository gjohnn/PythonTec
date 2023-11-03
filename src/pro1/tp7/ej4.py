'''4.	Escribe un programa que tome una lista de cadenas como entrada y 
las ordene en orden ascendente según su longitud.
Puedes utilizar el método de ordenamiento de inserción.'''

from functions import insertion_sort_by_length



new_list = ["hola" , "como estas" ,"chau" , "nos vemos" , "bye" , "hello" , "goodbye"]
insertion_sort_by_length(new_list)
print(new_list)