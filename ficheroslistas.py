cities = []


def add_city(cities_list):
    new_city = ""
    while new_city.lower() != "ok":
        new_city = input("Introduzca una ciudad. ")
        if new_city.lower() != "ok":
            cities_list.append(new_city)


def save_file(cities_list):
    string_cities = "$".join(cities_list)
    f = open("ficheroslistas.txt", "w")
    f.write(string_cities)
    f.close()


def read_file():
    try:
        f = open("ficheroslistas.txt", "r")
        string_cities = f.read()
        cities_list = string_cities.split("$")
        print(cities_list)
    except FileNotFoundError:
        print("No se ha encontrado el archivo.")


def show_menu():
    print("Seleccione entre las siguientes opciones: ")
    print("1. Mostrar ciudades")
    print("2. Añadir ciudad")
    print("3. Guardar archivo")


choice = -1

while choice != 0:

    show_menu()

    choice = int(input("> "))

    if choice == 1:
        read_file()
    elif choice == 2:
        add_city(cities)
    elif choice == 3:
        save_file(cities)
    else:
        pass
