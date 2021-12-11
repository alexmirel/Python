num1 = int(input("Introduzca el primer número. "))
num2 = int(input("Introduzca el segundo número. "))
num3 = int(input("Introduzca el tercer número. "))

max_num = 0
mid_num = 0
min_num = 0

num_sum = num1 + num2 + num3

if num1 > num2 and num1 > num3:
    max_num = num1
    if num2 > num3:
        mid_num = num2
        min_num = num3
    else:
        mid_num = num3
        min_num = num2
elif num2 > num1 and num2 > num3:
    max_num = num2
    if num1 > num3:
        mid_num = num1
        min_num = num3
    else:
        mid_num = num3
        min_num = num1
else:
    max_num = num3
    if num1 > num2:
        mid_num = num1
        min_num = num2
    else:
        mid_num = num2
        min_num = num1

print(f"El mayor número es {max_num}.")
print(f"El número intermedio es {mid_num}.")
print(f"El menor número es {min_num}.")
print(f"Los tres números suman {num_sum}.")
