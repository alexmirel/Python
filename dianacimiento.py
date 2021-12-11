import math

day = int(input("Introduce el día de tu cumpleaños. "))
month = int(input("Introduce el mes de tu cumpleaños. "))
year = int(input("Introduce el año de tu cumpleaños. "))

if month == 1:
    month == 13
    year -= 1
elif month == 2:
    month == 14
    year -= 1

op1 = math.trunc(((month+1)*3)/5)
op2 = math.trunc(year/4)
op3 = math.trunc(year/100)
op4 = math.trunc(year/400)
op5 = day + (month*2) + year + op1 + op2 - op3 + op4 + 2
op6 = math.trunc(op5/7)
op7 = op5 - (op6*7)

result = ""

if op7 == 0:
    result = "sábado"
elif op7 == 1:
    result = "domingo"
elif op7 == 2:
    result = "lunes"
elif op7 == 3:
    result = "martes"
elif op7 == 4:
    result = "miércoles"
elif op7 == 5:
    result = "jueves"
elif op7 == 6:
    result = "viernes"

print(f"Naciste un {result}.")
