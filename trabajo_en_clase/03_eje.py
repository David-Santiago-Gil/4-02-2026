numero = int(input("Escribe el numero: "))

if numero > 50 and numero % 2 == 0:
    print("El numero es par y mayor a 50")
elif numero > 50 and numero % 2 != 0:
    print("El numero es impar y mayor a 50")
elif numero <= 50 and numero % 2 == 0:
    print("El numero es par y menor o igual a 50")
else:
    print("El numero es impar y menor o igual a 50")