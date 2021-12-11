class Mes:
    nombre = ""
    temperatura_maxima = 0
    temperatura_minima = 0

    def temperatura_media(self):
        return (self.temperatura_maxima+self.temperatura_minima)/2

    def __str__(self):
        return f"Nombre: {self.nombre}\nTemperatura mínima: {self.temperatura_minima}\nTemperatura máxima: {self.temperatura_maxima}\nTemperatura media: {self.temperatura_media()}"
