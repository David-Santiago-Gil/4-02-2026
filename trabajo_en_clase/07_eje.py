edad = int(input("Escribe tu edad: "))
ciudadano = input("¿Eres ciudadano? (si/no): ")

if edad >= 18 and ciudadano == "si":
    print("Puedes votar y eres ciudadano ")
else:
    print("No puedes votar porque no eres mayor de 18 o no eres ciudadano.")