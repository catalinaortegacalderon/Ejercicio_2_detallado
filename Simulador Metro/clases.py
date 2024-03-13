class Metro:
    def __init__(self, numero_metro, posicion, direccion, color):
        self.numero_metro = numero_metro
        self.posicion = posicion
        self.pasajeros = []
        self.direccion = direccion
        self.en_estacion = False
        #agregar capacidad limitada de pasajeros
        self.capacidad_maxima = 250
        self.color = color


    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)

    def mover(self):
        if self.direccion == "izquierda" and self.posicion == 0:
            self.direccion = "derecha"
            self.posicion += 1

        elif self.direccion == "izquierda":
            self.posicion -= 1

        elif self.direccion == "derecha" and self.posicion == 47:
            self.direccion = "izquierda"
            self.posicion -= 1

        elif self.direccion == "derecha":
            self.posicion += 1


class Pasajero:
    def __init__(self, destino):
        self.destino = destino
        self.tiempo = 0
        self.direccion = ""
        self.tviaje = 0

    def aumentar_tiempo(self):
        self.tiempo += 1

    def aumentar_tiempo2(self):
        self.tviaje += 1

class Estacion:
    def __init__(self, posicion, color):
        self.posicion = posicion
        self.pasajeros = []
        self.color = color

    def agregar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)
    

