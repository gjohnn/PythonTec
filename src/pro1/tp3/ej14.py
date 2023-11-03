n1 = int(input("ingrese n1: "))
n2 = int(input("ingrese n2: "))

for i in range(n1,n2+1):
    if i%2==0:
        print(f'{i} es par')
    else:
        print(f'{i} es impar')
