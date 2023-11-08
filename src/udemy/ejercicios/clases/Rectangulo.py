class Rectangulo:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def perimeter(self):
        return (self.height+self.base) *2

    def area(self):
        return self.height*self.base

    def show_data(self):
        print(f"Perímetro: {self.perimeter()}")
        print(f"Area: {self.area()}")



rectangle = Rectangulo(15,3)
rectangle.show_data()
