num = int(input("Ingresa un número: "))
if num % 3 == 0 and num % 5 == 0:
    print("Es múltiplo de ambos (3 y 5)")
elif num % 3 == 0:
    print("Es múltiplo de 3")
elif num % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo ni de 3 ni de 5")