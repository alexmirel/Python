email = input("Introduzca su e-mail. ")

valid = True

if email.find("@") == -1:
    valid = False
elif email.find(".") == -1:
    valid = False
elif email.startswith("@") or email.endswith("@"):
    valid = False
elif email.startswith(".") or email.endswith("."):
    valid = False
elif email.find("@") != email.rfind("@"):
    valid = False
elif email[email.find("@"):].find(".") == -1:
    valid = False
elif not 2 <= len(email[(email.rfind(".")+1):]) <= 4:
    valid = False

if not valid:
    print("Incorrecto.")
else:
    print("Correcto.")
