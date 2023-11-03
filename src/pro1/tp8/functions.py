def number_of_digits(num , cont):
    if num // 10 ==0:
        cont=1
        return cont
    else:
        return cont+1 + number_of_digits(num/10 , cont)

def potency(base, numero):
    if base <= 1 or numero <= 0:
        return False
    # Calcula el logaritmo en base 'base' del número.
    log_result = math.log(numero, base)
    # Comprueba si el logaritmo es un número entero.
    print(f"Resultado: {base} elevado a la {int(log_result)}") if log_result.is_integer() else ("")
    return log_result.is_integer()

def find_equals(a, b, index=0, res=None):
    if res is None:
        res = []
    
    # Busca la primera ocurrencia de b en a, comenzando desde la posición actual (index)
    index = a.find(b, index)
    # Si se encuentra una ocurrencia, agrega la posición a la lista de resultados
    if index != -1:
        res.append(index)
        # Llamada recursiva para buscar más ocurrencias a partir de la posición siguiente
        find_equals(a, b, index + 1, res)
    return res

def even(n):
    if n == 1:
        print("1 es impar")
        return 
    if n%2!=0:
        print(f"{n} es impar")
        odd(n-1)
    else:
        odd(n)


def odd(n):
    if n == 1:
        even(n)
        return
    if n%2==0:
        print(f"{n} es par")
    else:
        even(n)

def encontrar_mayor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maximo_restante = encontrar_mayor(lista[1:])
        if lista[0] > maximo_restante:
            return lista[0]
        else:
            return maximo_restante