num = int(input("Introduzca un número. "))

while num != 1:
    if num % 2 == 0:
        num = int(num/2)
    else:
        num = num * 3 + 1
    print(num)
