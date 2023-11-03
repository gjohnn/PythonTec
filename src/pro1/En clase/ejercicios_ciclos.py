print("------------------------------------ EJ1 ------------------------------------")

#array de letras
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

move_place = int(input("Ingrese corrimiento: "))

for e in range(1, 6):
    #ingresar palabra que se tomara en minusculas
    word = input("Ingrese palabra: ").lower()
    word_list = list(word)

    for i in range(0,len(word)):
        for j in range(0,len(alphabet)):
            if word_list[i] == alphabet[(j)]:
                #reemplazar letra
                word_list[i] =alphabet[(j+move_place)%26]
                break
    #acomodar letras
    word_final = ""
    for k in word_list:
        word_final+=k
    #mostrar letras
    print(f"Mensaje para oficial {e}:",word_final)

print("------------------------------------ EJ2 ------------------------------------")
#EJ2
n=None
digit = None
numbers = []

while n != 0 or n<0:
    # ingresar n al array
    n = int(input("Ingrese n (0 para terminar): "))
    if n == 0:
        #cortar en 0 para que no sume 0 al array
        break
    numbers.append(n)

total_even = 0
total_odd = 0

for i in range(0, len(numbers)):
    quantity_even = 0
    quantity_odd = 0
    aux = numbers[i] #auxiliar
    while aux !=0:
        digit = aux%10
        if digit%2 == 0:
            # digit mod 2 = 0 entonces sumar 1
            quantity_even+=1
            total_even += 1
        else:
            # digit mod 3 = 0 entonces sumar 1
            quantity_odd+=1
            total_odd += 1
        aux=int(aux/10)
        #mostrar n con su cant de pares e impares
    print(f"{numbers[i]}: Par: {quantity_even} | Impar:{quantity_odd}")

print(f"Par: {total_even}")
print(f"Impar: {total_odd}")