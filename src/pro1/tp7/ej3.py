# Crear una lista de diccionarios con información sobre libros
from functions import ordenar_libros
libros = [
    {
        'titulo': 'El Gran Gatsby',
        'autor': 'F. Scott Fitzgerald',
        'anio_publicacion': 1925
    },
    {
        'titulo': 'Matar a un ruiseñor',
        'autor': 'Harper Lee',
        'anio_publicacion': 1960
    },
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'anio_publicacion': 1949
    },
    {
        'titulo': 'Cien años de soledad',
        'autor': 'Gabriel García Márquez',
        'anio_publicacion': 1967
    }
]

# Función para ordenar la lista de libros en función de un campo específico


# Ordenar la lista de libros por año de publicación
libros_ordenados_por_anio = ordenar_libros(libros, 'anio_publicacion')
print("Libros ordenados por año de publicación:")
for libro in libros_ordenados_por_anio:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de Publicación: {libro['anio_publicacion']}")

# Ordenar la lista de libros por autor
libros_ordenados_por_autor = ordenar_libros(libros, 'autor')
print("\nLibros ordenados por autor:")
for libro in libros_ordenados_por_autor:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año de Publicación: {libro['anio_publicacion']}")