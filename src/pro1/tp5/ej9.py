from functions import login

validation = False

for i in range(2,-1,-1):
    name_login = input("Ingrese usuario: ")
    password_login = input("Ingrese contraseña: ")
    
    user = {
        "name":name_login,
        "password":password_login
        }
    
    if login(user):
        validation = True
        break
    print(f"Quedan {i} intentos.") if i!=0 else print(" --- Intente más tarde. ---")

if validation:
    print(f"Bienvenido, {user["name"]}.")
