num = int(input("Ingresa un número: "))

if num > 0 and num < 100:
    print(" El número es positivo y menor que 100.")

elif num >= 100:
    print(" El número es positivo, pero es mayor o igual a 100.")

elif num == 0:
    print(" El número es cero (neutro).")

else:
    print(" El número es negativo.")