nombre=input("escribe tu nombre: ")
edad=int(input("Escriba su edad: "))

print("Tu nombre es: ",nombre)
print("Tu esdad es: ",edad)

print(f"tu nombre es: {nombre} y tu edad es: {edad}")

if edad>= 18:
    print("Es mayor de edad")
elif edad==18:
    print("Tiene 18 años")
else:
    print("Es menor de edad")