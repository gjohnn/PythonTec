"""El ANSES requiere clasificar a las personas que se jubilaran en el año de 2010. Existen tres tipos de
jubilaciones: por edad, por antigüedad joven y por antigüedad adulta.
- Las personas adscritas a la jubilación por edad deben tener 60 años o más y una antigüedad en su
empleo de menos de 25 años.
- Las personas adscritas a la jubilación por antigüedad joven deben tener menos de 60 años y una
antigüedad en su empleo de 25 años o más.
- Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad
en su empleo de 25 años o más.
Determinar en qué tipo de jubilación, quedara adscrita una persona."""


print("----- Jubilacion -----")

age = int(input("Ingrese edad: "))
years_worked = int(input("Ingrese antiguedad: "))

if age >= 60 and years_worked < 25:
    print("JUBILACION POR EDAD")
elif age < 60 and years_worked >= 25:
    print("JUBILACION POR ANTIGUEDAD JOVEN")
elif age >= 60 and years_worked >= 25:
    print("JUBILACION POR ANTIGUEDAD ADULTA")
