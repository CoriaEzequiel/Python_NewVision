'''
Simular lanzamiento de dados hasta obtener 6.
'''

import random
numero = 0
while numero != 6:
    numero = random.randint(1,6)
    print(f"Has sacado {numero}")

print("Has logrado sacar 6!")