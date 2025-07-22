'''
Imprimir tabla de multiplicar de un numero ingresado.
'''

numero = int(input("Ingrese su número"))
i = 1
while i <= 10 :
    print (f"{numero} x {i} = {numero * i}")
    i = i+1