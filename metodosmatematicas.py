def sum(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def show_menu():
    print("Seleccione una opción entre las siguientes: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Salir")


num1 = int(input("Introduzca el primer número. "))
num2 = int(input("Introduzca el segundo número. "))

choice = -1

while choice != 0:

    show_menu()

    choice = int(input("> "))

    result = None

    if choice == 0:
        print("Ha salido.")
        break
    elif choice == 1:
        result = sum(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == 2:
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == 4:
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Selección no válida.")

    answer = input("¿Desea introducir otros números? (s/n): ")

    if answer == "s":
        num1 = int(input("Introduzca el primer número. "))
        num2 = int(input("Introduzca el segundo número. "))
