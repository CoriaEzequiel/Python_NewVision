'''
Verificar si la palabra ingresada es "Python"
'''

palabra = str(input("Ingrese la palabra: "))

if palabra.lower() == "python":
    print('las palabras coinciden totalmente')
else:
    print('la palabra ingresada no coincide con "python"')