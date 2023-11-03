partidos = []

for i in range(0, 11):
    
    name_team = input("Nombre del equipo: ")
    row = []
    print(f"--------------- {name_team} -------------------")
    row.append(name_team)
    qty_defeats = 0
    qty_wins = 0
    qty_draws = 0
    for j in range(1, 11):
        goals = int(input(f"Ingrese goles F|C {j}:"))
        if goals < 0:
            qty_defeats += 1
        elif goals > 0:
            qty_wins += 1
        elif goals == 0:
            qty_draws += 1
        row.append(goals)
    print(f"Partidos ganados: {qty_wins}")
    print(f"Partidos empatados: {qty_draws}")
    print(f"Partidos perdidos: {qty_defeats}")
    points = 3*qty_wins + qty_draws
    print("----------------------------------")
    print(f"Puntos: {points}")
    print("----------------------------------")
    partidos.append(row)

print("TABLA")

for e in partidos:
    print(e)
