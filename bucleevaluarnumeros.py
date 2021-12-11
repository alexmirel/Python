answer = True

while answer:
    num = int(input("Introduzca un número. "))

    if num > 0:
        print("El número es positivo.")
    elif num < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")
    print()

    answer = input("¿Desea continuar? (s/n): ")

    if answer == "s":
        answer = True
    else:
        answer = False
