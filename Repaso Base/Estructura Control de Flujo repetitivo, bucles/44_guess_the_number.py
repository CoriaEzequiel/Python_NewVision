'''
    Generar numero aleatorio del 1 al 10.
    pedir al usuario adivinar el número hasta que sea correcto.     Bucle infinito hasta que termina.
'''

import random
numero_secreto = random.randint(1,10)
intentos = 0

while True:
    intento = int(input('Adivina el número: '))
    intentos = intentos+1
    if intento == numero_secreto:
        print(f"Exito! Adivinar el número secreto tomó {intentos} intentos.")
        break