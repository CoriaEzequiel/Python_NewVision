'''
determinar si el año es bisiesto

regla: divisible por 4, no divisible por 100, divisible por 400
'''

age = int(input("Inserte año que desee:"))
if (age % 4 == 0 and age % 100 != 0) or (age % 400 == 0):
    print('Es un año bisiesto')
else:
    print('No es bisiesto')