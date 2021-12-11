import math

dni = input("Introduzca su número del DNI sin la letra. ")

dni_letters = "TRWAGMYFPDXBNJZSQVHLCKET"

if dni.isdigit():
    result = (int(dni)-math.trunc(int(dni)/23)*23)
    print(dni_letters[result])
else:
    print("Debes introducir un número.")
