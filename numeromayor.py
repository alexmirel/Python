num1 = int(input("Introduzca un número. "))
num2 = int(input("Introduzca otro número. "))

if num1 > num2:
    print(f"{num1} es mayor que {num2}.")
elif num1 < num2:
    print(f"{num2} es mayor que {num1}.")
else:
    print("Has introducido el mismo número dos veces.")
