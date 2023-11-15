class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_data(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")

    def __str__(self):
        return (f"Persona [Name: {self.name}, Age: {self.age}]")


class Empleado(Persona):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()} Salary: {self.salary}"


if __name__ == "__main__":
    empleado1 = Empleado("Juan", 19, 5000)
    empleado1.show_data()
