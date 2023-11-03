from functions import word_dictionary

word = input("Ingrese palabra: ")

letters = word_dictionary(word)
print(f"Cantidad de letras: {len(letters)}")
print(letters)