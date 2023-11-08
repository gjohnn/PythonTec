class Cuenta:
    def __init__(self, titular, qty):
        self.titular = titular
        self.qty = qty if qty > 0 else 0

    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Dinero disponible: {self.qty}")

    def ingresar(self):
        ingreso_dinero = float(input("Ingrese monto a ingresar: "))
        self.qty += ingreso_dinero

    def retirar(self):
        retiro_dinero = float(input("Ingrese monto a retirar: "))
        while retiro_dinero < 0 or retiro_dinero > self.qty:
            retiro_dinero = float(input("Ingrese monto a retirar: "))
        self.qty -= retiro_dinero


titular = input("Nombre del titular: ")
while titular == None or titular == " ":
    titular = input("Nombre del titular: ")
money = float(input("Dinero del titular: "))

example = Cuenta(titular, money)

while True:
    print("-----------------------------------")
    example.mostrar()

    print(" -- Menu -- ")
    print("1) Ingresar dinero")
    print("2) Retirar dinero")
    print("0) Salir")
    option = int(input("Ingrese opcion: "))
    if option == 0:
        print("Adios!")
        break
    elif option == 1:
        example.ingresar()
    elif option == 2:
        example.retirar() if example.qty != 0 else print("No hay dinero en la cuenta.")
