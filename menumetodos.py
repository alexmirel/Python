import time


def menu():
    print("Seleccione entre las siguientes opciones: ")
    print("1. Comprobar si un año es bisiesto")
    print("2. Comprobar si un número es narcisista")
    print("3. Mostrar todos los años bisiestos a partir de un año hasta el año actual")
    print("0. Salir")


def leap(year):
    is_leap = False
    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0:
            is_leap = False
            if year % 400 == 0:
                is_leap = True
    return is_leap


def narcissistic(number):
    number = str(number)
    length = len(number)
    sum = 0
    narcissistic = False
    for i in range(length):
        digit = int(number[i])
        power = digit ** length
        sum += power
    if sum == int(number):
        narcissistic = True
    return narcissistic


def leap_years(year):
    import time
    year_now = int(time.strftime("%Y"))
    for i in range(year, year_now+1):
        leap(i)
        if leap(i):
            print(i)
