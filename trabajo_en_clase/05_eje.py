usuario = input("Usuario: ")
clave = input("Contraseña: ")
if usuario == "admin" and clave == "1234":
    print("Acceso concedido")
elif usuario != "admin":
    print("Usuario incorrecto")
else:
    print("Contraseña incorrecta")