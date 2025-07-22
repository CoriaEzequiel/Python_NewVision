'''
Solicitar número y contar dígitos
'''


numero = int(input("Ingrese un número: "))
original = numero
contador = 0

if numero == 0:
    contador = 1
else:
    while numero != 0:
        numero //= 10
        contador += 1

print(f"Los dígitos de {original} son {contador} dígitos")