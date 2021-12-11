isbn = input("Introduzca el ISBN. ")

isbn_sum = 0

if isbn.isdigit and len(isbn) == 10:
    for i in range(len(isbn)):
        isbn_sum += int(isbn[i]) * (i+1)
    if isbn_sum % 11 == 0:
        print("Correcto.")
    else:
        print("Incorrecto.")
else:
    print("Debe introducir un número de diez caracteres.")
