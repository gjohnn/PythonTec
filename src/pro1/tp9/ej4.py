class Contact:
    def __init__(self,name,number,email):
        self.name = name
        self.number = number
        self.email = email


contacts = []
def add_contact():
    name = input("Nombre: ").lower()
    while name == None or name == " ":
        name = input("Nombre: ").lower()
    number = int(input("Número: "))
    email = input("Ingrese mail: ")
    while True:
        if not "@" in email:
            email = input("Ingrese mail: ")
        else:
            break
    new_contact = Contact(name, number,email)
    contacts.append(new_contact)

def show_contacts():
    for i in range(0,len(contacts)):
        print(f"Nombre: {(contacts[i].name).title()}")
        print(f"Telefono: {contacts[i].number}")
        print(f"Email: {contacts[i].email}")
        print("--")

def find_contact(name):
    for e in contacts:
        if e.name ==name:
            print(f"Nombre: {(e.name).title()}")
            print(f"Número: {e.number}")
            print(f"Email: {e.email}")



def edit_contact(name):
    for e in contacts:
        if e.name == name:
            new_name = input("Nuevo nombre: ").lower()
            while new_name == None or new_name == " ":
                new_name = input("Nuevo nombre: ").lower()
            new_number = int(input("Nuevo número: "))
            new_email = input("Nuevo mail: ")
            while True:
                if not "@" in new_email:
                    new_email = input("Nuevo mail: ")
                else:
                    break
            e.name = new_name
            e.number = new_number
            e.email = new_email
            print("Contacto editado con éxito.")
            return
    print("Contacto no encontrado.")

while True:
    print(" -- Menu -- ")
    print("1) Añadir contacto")
    print("2) Lista de contactos")
    print("3) Buscar de contacto")
    print("4) Editar contacto")
    print("0) Cerrar agenda")
    option = int(input("Ingrese opcion: "))
    print("------------")
    if option == 0:
        print("Adios!")
        break
    elif option == 1:
        add_contact()
    elif option == 2:
        show_contacts() if len(contacts)>0 else print("No hay contactos.")
        print("------------")
    elif option == 3:
        name = input("Ingrese nombre del contacto a buscar: ").lower()
        find_contact(name)
    elif option == 4:
        name = input("Ingrese nombre del contacto a editar: ").lower()
        edit_contact(name)
input()