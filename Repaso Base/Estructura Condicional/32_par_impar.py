'''
Pedir número y comprobar si es un número par o impar.
'''

numero = int(input("Ingrese un número: " ))
if numero % 2 == 0:
    print(numero, "Es un número par")
else: print(numero,"Es un numero impar")