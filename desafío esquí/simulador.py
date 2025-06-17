from clases import simulador
import random
import math
import time
mi_carrera = simulador(0, 20, 0)
inicio = time.time()
while True:
    if mi_carrera.get_posicion() == 19:
        final = time.time()
        tiempo = str(final -inicio)
        print ("¡ganaste! en " + tiempo + " segundos")
        break
    sig_vuelta = random.randint(1,20)
    mi_carrera.set_curva(sig_vuelta)
    print(mi_carrera)
    entrada=math.floor(float(input("elija la velocidad a la que tomará la curva")))
    mi_carrera.set_velocidad(entrada)
    if entrada < (mi_carrera.get_curva()) or entrada == mi_carrera.get_curva():
        mi_carrera.set_posicion(mi_carrera.get_posicion()+1)
    elif entrada > (mi_carrera.get_curva() + mi_carrera.get_curva() * 0.2):
        print("caíste por el precipicio hacia tu muerte")
        break
    elif entrada > (mi_carrera.get_curva()) and entrada < (mi_carrera.get_curva() + mi_carrera.get_curva() * 0.2):
        mi_carrera.set_posicion(mi_carrera.get_posicion()-1)