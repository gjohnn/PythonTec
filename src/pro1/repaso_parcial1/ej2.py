import random
# Lista de palabras
words = ["python", "programacion", "computadora", "codigo", "aprendizaje"]
word = random.choice(words)
intentos = 6
print("--- EL AHORCADO ---")
word_guessing = ["_"]*len(word)
print(f"Palabra a adivinar: {"".join(word_guessing)}")
while intentos > 0 :
    letter = input("Ingrese letra: ").lower
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                word_guessing[i] = letter
                print("".join(word_guessing))
    else:
        print("Ups! No se encuentra esa letra!")
        intentos-=1
    if "".join(word_guessing) == word or letter == word:
        print("Lo lograste!")
        break

if intentos == 0:
    print(f"Te quedaste sin intentos! La palabra era: {word}")