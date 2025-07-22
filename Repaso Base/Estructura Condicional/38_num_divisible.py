'''
Determinar si el número es divisible entre 5 y 7
'''

numero = int(input("Ingrese número que desee: "))

if numero % 5 == 0 and numero % 7 == 0 :
    print(numero, "Es divisible entre 5 y 7")
else:
    print(numero,"No es divisible entre 5 y 7")