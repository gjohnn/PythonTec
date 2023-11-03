import random

lives = 6
defined_words = ["ARGENTINA", "ITALIA", "FRANCIA", "BOLIVIA", "BRASIL"]
#Con random.choice agarro cualquier elemento del array al azar
random_word = random.choice(defined_words)
print(" ------- JUEGO DEL AHORCADO ------- ")
#Crear array segun la cantidad de letras de random_word
word_guess = ["_"]*len(random_word)
print('Letras: ', " ".join(word_guess))

while lives!=0:
    letter = input("Ingrese letra: ").upper()
   #Corrobo si existe, si no se resta una vida
    if letter in random_word:
        #si el usuario ingresa la palabra completa gana el juego directamente
        if letter == random_word:
            for i in range(0, len(random_word)):
                word_guess[i] = random_word[i]
            print(" ".join(word_guess))
            break
        for i in range(0, len(random_word)):
            #Por cada letra se verifica si es igual a lo que ingreso el usuario
           if letter == random_word[i]:
               #Reemplaza el _ por la letra que corresponde en dicho lugar
               word_guess[i] = letter
    else:
       lives-=1
    print('Palabra: ', " ".join(word_guess))
    #Utilizo .join para juntar todos los valores de un array y asi realizar una comparacion directa con la palabra random
    if "".join(word_guess) == random_word or letter == random_word:
        break
#Si la cantidad de vidas bajo a cero muestro el mensaje de que perdió, si no que no ganó
if lives == 0:
    print(f"Perdiste! La palabra era: {random_word}")
else:
    print("Ganaste!!!!!!")