x = 0

while x<31:
    if x == 15:
        print(f"Se rompió la ejecucion cuando x valía: {x}")
        break
    if x == 4 or x == 6 or x==10:
        print(f"Se saltó el valor {x}")
    else:
        print(x)
    x+=1
