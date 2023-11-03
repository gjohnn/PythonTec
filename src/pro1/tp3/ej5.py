investment = float(input("Ingrese cantidad a invertir: "))
annual_interest = float(input("Ingrese interés anual: "))
qty_year = int(input("Ingrese cantidad de años: "))

total_investment = investment + (investment * (annual_interest/100)) 

for i in range(1, qty_year+1):
    print(f"Inversión de año {i}: {total_investment*qty_year}")