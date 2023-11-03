
passengers = [("juan", 45720526, "mendoza"),("papu", 12312312, "guadalajara")]

for x in passengers:
    print(f"Nombre: {x[0]}") 
    print(f"DNI: {x[1]}") 
    print(f"Destino: {x[2]}") 
    print("-------------------------------------------------------")


cities_country = [("mendoza","argentina"),("guadalajara", "mexico")]

for place in cities_country:
    print(f"Ciudad: {place[0]}")
    print(f"País: {place[1]}")
    print("-------------------------------------------------------")