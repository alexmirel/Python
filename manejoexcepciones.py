def divide():
    try:
        num1 = int(input("Introduzca el dividendo. "))
        num2 = int(input("Introduzca el divisor. "))
        result = num1 / num2
        print(result)
    except ValueError:
        print("Debe introducir un número.")
    except ZeroDivisionError:
        print("El divisor no puede ser cero.")
    except:
        print("Ha ocurrido un error.")
    finally:
        print("Fin del programa.")


divide()
