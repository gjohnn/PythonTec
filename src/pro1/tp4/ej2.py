lineas = []

while True:
    linea = input("Ingrese una línea (o presione Enter para finalizar): ")
    if not linea:
        break
    lineas.append(linea)

for linea in lineas:
    print(linea.upper())