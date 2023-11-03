word = input("Ingrese palabra: ")
letter = input("Ingrese letra: ")
counter = 0

for i in range(0,len(word)):
    if letter == word[i]:
        counter+=1

print(f"La letra '{letter}' aparece {counter} vez/veces")