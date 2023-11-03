year_one = int(input("Ingrese año 1: "))
year_two = int(input("Ingrese año 2: "))
while year_two < year_one:
    year_two = int(input("Ingrese año 2 (mayor a año 1): "))

for i in range(year_one, year_two+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        print(i)