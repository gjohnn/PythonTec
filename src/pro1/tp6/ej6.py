primary = []
secondary = []

while True:
    student = input(
        "Nombre del alumno de escuela PRIMARIA ('x' para terminar): "
    ).lower().strip()
    if student == "x":
        break
    primary.append(student)


while True:
    student = input(
        "Nombre del alumno de escuela SECUNDARIA ('x' para terminar): "
    ).lower().strip()
    if student == "x":
        break
    secondary.append(student)

print("------------")

for e in primary:
    print("Alumno de primaria:", e)
print("------------")
for e in secondary:
    print("Alumno de secundaria:", e)
print("------------")

if len(primary) >= len(secondary):
    for p in primary:
        if p in secondary:
            print(f"El nombre {p} se repite")
        else:
            print(f"El nombre {p} NO se repite")

else:
    for s in secondary:
        if s in primary:
            print(f"El nombre {s} se repite")
        else:
            print(f"El nombre {p} NO se repite")
