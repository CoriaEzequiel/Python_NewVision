import random

valores = ['A', '2','3', '4', '5', '6', '7', '8', '9', '10', '11', 'J', 'Q', 'K']
palos = ['♠', '♥', '♦', '♣']

baraja = [valor + palo for valor in valores for palo in palos]
random.shuffle(baraja)

jugadores = 3
cartas_jug = 5


manos = [[] for _ in range(jugadores)] #listas de 'manos vacías' para cada jugador.

# Repartir una carta a cada jugador por turno
for i in range(cartas_jug):
    for j in range(jugadores):
        carta = baraja.pop(0)  
        manos[j].append(carta) 


for i, mano in enumerate(manos):  #recorre lista manos, devuelve índice de jugador y mano
    print(f"Jugador {i+1}: {mano}")