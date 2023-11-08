class Cubo:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def volume(self):
        return  self.x * self.y *self.z
    def show_data(self):
        print(f"Volumen: {self.volume()}")


cube1 = Cubo(3,5,6)
cube1.show_data()


