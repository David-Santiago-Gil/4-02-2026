n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
if n1 == n2:
    print("Los números son iguales")
elif (n1 + n2) > 100:
    print("Los números son diferentes, pero su suma es mayor a 100")
else:
    print("No son iguales y su suma es 100 o menos")