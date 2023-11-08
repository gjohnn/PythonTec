class Persona:
    id_person = 1
    def __init__(self, name, surname, age, id_person=id_person):
        self._name = name
        self.surname = surname
        self.age = age
        self.id_person = Persona.id_person
        Persona.id_person += 1
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def show_data(self):
        print(f"ID: {self.id_person} | Nombre: {self._name} {self.surname} | Edad: {self.age}")

    def __del__(self):
        print(f"Object ID: {self.id_person} | DELETED")

if __name__ == "__main__":
    print("CLASS PERSONA CODE")
    print(":)")