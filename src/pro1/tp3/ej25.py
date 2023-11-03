n = int(input("Ingrese n para ver su factorial: "))

if n != 0 and n>0:
    for i in range(1,n):
        n = n*i
else:
    n = 1


print(n)