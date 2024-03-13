import random
from clases import Metro, Pasajero, Estacion
import linea_RV

#falta chequear capacidad max

#codigo antiguo
E = [1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 0 ,
0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1]
# nueva estacion
E_color = linea_RV.E

numero_estaciones = []
for i in range(len(E)):
    if E[i] == 1:
        numero_estaciones.append(i)

M1 = Metro(1, 0, "izquierda", "rojo")
M2 = Metro(2, 16, "derecha", "verde")
M3 = Metro(3, 32, "derecha", "rojo")
M4 = Metro(4, 16, "izquierda", "verde")
M5 = Metro(5, 32, "izquierda", "rojo")
M6 = Metro(6, 47, "derecha", "verde")
# se agregan dos metros
M7 = Metro(7, 24, "izquierda", "rojo")
M8 = Metro(8, 24, "derecha", "verde")

Metros = [M1, M2, M3, M4, M5, M6]

#codigo antiguo
E1 = Estacion(0, "mixto")
E2 = Estacion(7, "rojo")
E3 = Estacion(14, "verde")
E4 = Estacion(20, "rojo")
E5 = Estacion(27, "verde")
E6 = Estacion(33, "rojo")
E7 = Estacion(38, "verde")
E8 = Estacion(47, "mixto")
Estaciones = [E1, E2, E3, E4, E5, E6, E7, E8]

Estaciones_verdes = [E3, E5, E7]
Estaciones_rojas = [E2, E4, E6]
Estaciones_mixtas = [E1, E8]
# sumar estas listas

#otra manera de crear estaciones: con un for, utilice la logica del codigo antiguo pero es mejor un for

tiempo_total = 0

pasajeros_totales = 0

tiempo_de_viaje_total = 0

tiempo_de_espera_total = 0

esperantes_confirmados = 0

pasajeros_activos = []
    
print(f"Tiempo: {tiempo_total}")
for metro in Metros:
    print(f"    Metro en posición {metro.posicion} avanza hacia {metro.direccion} con {len(metro.pasajeros)} pasajeros")
print("")
for estacion in Estaciones:
    print(f"    Estación en posición {estacion.posicion} tiene {len(estacion.pasajeros)} pasajeros esperando en el anden")
print("")

# aca se cambio del tiempo de simulacion de 600 (en el range, 601) a 16 horas (960 minutos)
for tiempo_total in range(1,961):
    for pasajero in pasajeros_activos:
        pasajero.tiempo += 1
        for metro in Metros:
            if pasajero in metro.pasajeros and pasajero.destino == metro.posicion:
                metro.pasajeros.remove(pasajero)
                pasajeros_totales += 1
                tiempo_de_viaje_total += pasajero.tiempo 
                pasajeros_activos.remove(pasajero)
    
    #se cambio el radint de 10 a 20
    for estacion in Estaciones:
        n = random.randint(0, 20)
        for i in range(n):
            while True:
                #estacion_final = random.choices(numero_estaciones)[0]
                if estacion.color == "rojo":
                    estacion_final = random.choice(Estaciones_rojas + Estaciones_mixtas).posicion
                elif estacion.color == "verde":
                    estacion_final = random.choice(Estaciones_verdes + Estaciones_mixtas).posicion
                else:
                    estacion_final = random.choice(numero_estaciones)
                if estacion_final != estacion.posicion:
                    break
            pasajero_nuevo = Pasajero(estacion_final)
            if pasajero_nuevo.destino > estacion.posicion:
                pasajero_nuevo.direccion = "derecha"
            else:
                pasajero_nuevo.direccion = "izquierda"

            estacion.agregar_pasajero(pasajero_nuevo)
            pasajeros_activos.append(pasajero_nuevo)
            
    # recorrer todos los trenes        
    for metro in Metros:
        # recorrer todas las estaciones
        for estacion in Estaciones:
            # ver si hay un tren en una estacion
            if metro.posicion == estacion.posicion:
                # todas las personas en la estacion
                # agregue esta linea de abajo
                if estacion.color == "mixto" or estacion.color == metro.color:
                    for pasajero in estacion.pasajeros:
                        if metro.posicion == 0:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
                        elif metro.posicion == 47:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
                        elif pasajero.direccion == metro.direccion:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
        # todas las personas del metro
        for pasajero in metro.pasajeros:
            if pasajero.destino == metro.posicion:
                metro.pasajeros.remove(pasajero)
                pasajeros_totales += 1
                tiempo_de_viaje_total += pasajero.tiempo
                try:
                    pasajeros_activos.remove(pasajero)
                except ValueError:
                    pass

        if metro.en_estacion == False:
            metro.mover()
            # aca estai obligado a hacer doble for por la implemenracion pero es poco eficiente
            for estacion in Estaciones:
                for metro in Metros:
                    if metro.color == estacion.color or estacion.color == "mixto": 
                        metro.en_estacion = True

        # aca se repite codigo, se suben y bajan pasajeros dos veces (solo se hace una pero se revisa dos)
        elif metro.en_estacion:
            metro.en_estacion = False
            for estacion in Estaciones:
                if metro.posicion == estacion.posicion:
                    for pasajero in estacion.pasajeros:
                        if metro.posicion == 0:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
                        elif metro.posicion == 47:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
                        elif pasajero.direccion == metro.direccion:
                            metro.agregar_pasajero(pasajero)
                            estacion.pasajeros.remove(pasajero)
                            tiempo_de_espera_total += pasajero.tiempo
                            esperantes_confirmados += 1
                    
    tiempo_total += 1
    
    
    print(f"Tiempo: {tiempo_total}")
    for metro in Metros:
        print(f"    Metro en posición {metro.posicion} avanza hacia {metro.direccion} con {len(metro.pasajeros)} pasajeros")
    print("")
    for estacion in Estaciones:
        print(f"    Estación en posición {estacion.posicion} tiene {len(estacion.pasajeros)} pasajeros esperando en el anden")
    print("")
    
    

    
    
print(f"El tiempo de viaje promedio es de: {tiempo_de_viaje_total/pasajeros_totales}")
print(f"El tiempo de espera promedio es de: {tiempo_de_espera_total/esperantes_confirmados}")
