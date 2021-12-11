names = []


def show_names(names_list):
    for i in range(len(names_list)):
        print(str(i+1) + ". " + names_list[i])


def add_names():
    name = ""
    while name.lower() != "ok":
        name = input("Introduzca un nombre. ")
        if name.lower() != "ok":
            names.append(name)
    else:
        show_names(names)


def delete_name(index, names_list):
    names_list.pop(index)


def reset_list(names_list):
    names_list.clear()
    print("Se han eliminado todos los nombres de la lista.")


def show_menu():
    print("Seleccione entre las siguientes opciones: ")
    print("0. Salir")
    print("1. Añadir nombres")
    print("2. Eliminar nombre")
    print("3. Comenzar de nuevo")


choice = -1

try:
    while choice != 0:

        show_menu()

        choice = int(input("> "))

        if choice == 0:
            break
        elif choice == 1:
            add_names()
        elif choice == 2:
            show_names(names)
            index = int(input("Introduzca la posición del nombre. "))-1
            delete_name(index, names)
            show_names(names)
        elif choice == 3:
            reset_list(names)
        else:
            print("Selección inválida.")
except ValueError:
    print("Selección inválida.")
except IndexError:
    print("El índice no es válido.")
