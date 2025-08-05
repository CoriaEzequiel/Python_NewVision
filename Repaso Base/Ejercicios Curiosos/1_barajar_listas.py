'''
función shuffle del módulo random
'''

import random

#2 listas
valores = [
    'A', '2','3', '4', '5', '6', '7', '8', '9', '10', '11', 'J', 'Q', 'K'
]

palos = [
    '♠', '♥', '♦', '♣'
]

#comprensión de listas para crear cartas uniendo valor con cada palo de la baraja

baraja = [
    valor + palo
    for valor in valores
    for palo in palos
]

#print(baraja) 

random.shuffle(baraja)  #mezcla de la baraja con función shuffle del mod random.
print(baraja)

jugadores = 3
cartas_jug = 5

for i in range(jugadores):      #slices de la baraja
    mano = baraja[
        i * cartas_jug :
        (i+1) * cartas_jug
    ]
    print(f"Jugador{i+1}:{mano}")