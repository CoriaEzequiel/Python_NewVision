'''
Simular lanzamiento de dado hasta obtener 6,
con opción de volver a tirar.
'''

import random

while True:
    numero = random.randint(1, 6)
    print(f"Has sacado {numero}")
    
    if numero == 6:
        print("Has logrado sacar 6! Fin del juego.")
        break

    jugar = input("¿Querés volver a tirar? (S/N): ")
    if jugar.lower() == 'n':
        print("Juego finalizado. Hasta pronto!")
        break