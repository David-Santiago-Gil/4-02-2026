numero = int(input("Escribe un numero:"))

if numero > 10:
    print("El numero es mayor que 10")
    if numero >30:
        print("Ademas el numero es mayor que 30")
    elif numero >20:
        print("Ademas el numero es mayor que 20")
        if True:
            print("linea de ejemplo")
    else:
        print("Ademas el numero es menor que 21")
else:
    print("El numeor es meenor que 10")
    