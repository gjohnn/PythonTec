class Persona:
    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni

    def mayorDeEdad(self):
        es_mayor = False
        if self.age >= 18:
            es_mayor = True
        return es_mayor

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age} | Es mayor de edad") if self.mayorDeEdad() else print(f"Edad: {self.age} | Es menor de edad")
        print(f"DNI: {self.dni}")


def validateDNI():
    while True:
        dni = int(input("Ingrese dni: "))
        if len(str(dni)) > 6 and len(str(dni)) < 9:
            break
        else:
            print("DNI no existente!")
    return dni


name = input("Ingrese nombre: ")
age = int(input("Ingrese edad: "))
dni = validateDNI()

person = Persona(name, age, dni)

person.mostrar()
