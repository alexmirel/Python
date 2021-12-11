from menumetodos import menu, leap, narcissistic, leap_years

choice = "choice"

while choice != "0":

    menu()

    choice = input("> ")

    if choice.isdigit():
        if choice == "0":
            break
        elif choice == "1" or choice == "2" or choice == "3":
            number = input("Introduzca el número/año. ")
            if number.isdigit():
                number = int(number)
                if choice == "1":
                    leap(number)
                    if leap(number):
                        print(f"El año {number} es bisiesto.")
                    else:
                        print(f"El año {number} no es bisiesto.")
                elif choice == "2":
                    narcissistic(number)
                    if narcissistic(number):
                        print(f"El número {number} es narcisista.")
                    else:
                        print(f"El número {number} no es narcisista.")
                else:
                    leap_years(number)
            else:
                print("Debe introducir un número.")
            print()
    else:
        print("Selección incorrecta.")
        print()
