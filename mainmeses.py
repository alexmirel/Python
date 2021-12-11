from meses import Mes
import random

meses = []

for i in range(1, 13):
    mes = Mes()
    mes.nombre = "Mes " + str(i)
    mes.temperatura_minima = random.randint(0, 10)
    mes.temperatura_maxima = random.randint(20, 40)
    meses.append(mes)

for mes in meses:
    print(mes, end="\n\n")
