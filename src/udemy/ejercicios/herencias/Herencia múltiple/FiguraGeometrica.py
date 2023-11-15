class FiguraGeo:
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho

    def __str__(self):
        return f"Área: {self.altura * self.ancho}"


class Color:
    def __init__(self, color):
        self.color = color


class Cuadrado(FiguraGeo, Color):
    def __init__(self, lado, color):
        FiguraGeo.__init__(self, lado, lado)
        Color.__init__(self, color)
    def calculo_area(self):
        return f'Área: {self.ancho * self.altura} Color: {self.color}'

cuadrado1 = Cuadrado(5, "Verde")
print(cuadrado1.calculo_area())