class Vehiculo:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "Color: " + self.color + ", Ruedas: " + str(self.wheels)


class Coche(Vehiculo):
    def __init__(self,color,wheels,velocity):
        super().__init__(color,wheels)
        self.velocity = velocity
    def __str__(self):
        return super().__str__() + ", Velocidad (Km/h): "+ str(self.velocity)

class Bicicleta(Vehiculo):
    def __init__(self,color,wheels,type):
        super().__init__(color,wheels)
        self.type = type
    def __str__(self):
        return super().__str__() +", Tipo: "+self.type

vehiculo = Vehiculo("Rojo", 4)
print(f"Vehiculo | {vehiculo}")
coche = Coche("Verde", 4, 40)
print(f"Coche | {coche}")
bicicleta = Bicicleta("Amarillo", 2,"BMX")
print(f"Bicicleta | {bicicleta}")