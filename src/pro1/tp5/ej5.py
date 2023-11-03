from functions import temp_average

qty_days = int(input("Ingrese cantidad de días: "))

for i in range (1,qty_days+1):
    print(f"-- Día {i} --")
    temp_max = float(input("Ingrese temperatura máxima: "))
    temp_min = float(input("Ingrese temperatura mínima: "))
    print(f"-- Temperatura media: {temp_average(temp_max,temp_min)}°C --")