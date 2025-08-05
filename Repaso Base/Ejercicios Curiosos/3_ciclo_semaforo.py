import itertools
import time

semaforo = ['verde','amarillo','rojo']
ciclo = itertools.cycle(semaforo)

for color in ciclo:
    print(color)
    time.sleep(1)