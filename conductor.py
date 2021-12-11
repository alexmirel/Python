from coche import Coche

mi_coche = Coche("Opel", "Astra")

opcion = -1

while opcion != 0:
    print("0. Salir")
    print("1. Arrancar")
    print("2. Acelerar")
    print("3. Frenar")
    print("4. Detener")

    opcion = int(input("> "))

    if opcion == 0:
        break
    elif opcion == 1:
        mi_coche.arrancar()
    elif opcion == 2:
        mi_coche.acelerar()
    elif opcion == 3:
        mi_coche.frenar()
    elif opcion == 4:
        mi_coche.detener()
    else:
        print("Selección incorrecta.")
        