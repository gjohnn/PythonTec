class Triangle:
    def __init__(self,sideA,sideB,sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    def show_sides(self):
        print(" -- Valores --")
        print(f"LADO A: {self.sideA}")
        print(f"LADO B: {self.sideB}")
        print(f"LADO C: {self.sideC}")

    def type_of_triangle(self):
        print(" ----------------- ")
        type_of_tri = ""
        if self.sideA == self.sideB and self.sideA == self.sideC:
            type_of_tri = "Equilatero"
        elif  self.sideA == self.sideB or self.sideA == self.sideC or self.sideB == self.sideC:
            type_of_tri = "Isósceles"
        else:
            type_of_tri = "Escaleno"
        print(f"Tipo de Triangulo: {type_of_tri}")

lado1 = float(input("Ingrese lado A: "))
lado2 = float(input("Ingrese lado B: "))
lado3 = float(input("Ingrese lado C: "))

triangle = Triangle(lado1,lado2,lado3)

triangle.show_sides()

triangle.type_of_triangle()