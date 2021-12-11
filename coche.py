class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.en_marcha = False
    
    def arrancar(self):
        if not self.en_marcha:
            self.en_marcha = True
            print("Has arrancado el coche.")
        else:
            print("El coche ya está arrancado.")

    def detener(self):
        if self.en_marcha:
            self.en_marcha = False
            print("Has detenido el coche.")
        else:
            print("El coche no está arrancado.")

    def acelerar(self):
        if self.en_marcha:
            self.velocidad += 20
            print(f"La velocidad es {self.velocidad}.")
        else:
            print("El coche no está arrancado.")

    def frenar(self):
        if self.velocidad >= 20:
            self.velocidad -= 20
            print(f"La velocidad es {self.velocidad}.")
        else:
            print("El coche no está en movimiento.")

