class Aritmetica:
    """
    Clase para sumar,restar,etc
    """
    def __init__(self, opA, opB):
        self.opA = opA
        self.opB = opB

    def sum(self):
        return self.opA + self.opB

    def minor(self):
        return self.opA - self.opB

    def xtimes(self):
        return self.opA * self.opB

    def divition(self):
        if self.opB != 0:
            return self.opA / self.opB
        else:
            return None


aritmetica = Aritmetica(15, 10)
print(f"Suma: {aritmetica.sum()}")
print(f"Resta: {aritmetica.minor()}")
print(f"Multiplicacion: {aritmetica.xtimes()}")
print(f"Division: {aritmetica.divition()}")
