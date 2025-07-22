'''
Simular un lanzamiento de moneda
'''

import random

while True:
    moneda = random.randint(1,2)
    if moneda == 1:
        print ("Cara")
    else:
        print("Cruz")
    jugar = input ("Volver a lanzar? S/N")
    if jugar.lower() == 'n':
        break
print ("Gracias por jugar! Hasta pronto.") 