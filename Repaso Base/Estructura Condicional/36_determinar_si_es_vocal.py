'''
Pedir un caracter y determinar si es vocal
'''

caracter = str(input("Ingrese un caracter: "))
vocales =['a','e','i','o','u']

if caracter.lower() in vocales:
    print("Es Vocal")
else :
    print("No es Vocal")