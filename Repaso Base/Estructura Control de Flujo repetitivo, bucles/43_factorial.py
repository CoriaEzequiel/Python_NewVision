'''
Solicitar ingresar número e imprimir factorial X!
'''

numero = int(input("Ingrese un número: "))
factorial = 1
i = 1
while i <= numero:
    factorial = factorial * i
    i= i+1
print("El resultado del factorial es: ", factorial)