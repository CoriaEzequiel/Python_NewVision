'''
solicitar ingresar un número N e imprimir suma de todos los números desde 1 a N
Variable suma
variable i
'''

numero = int(input("Ingresa un número: "))
suma = 0
i=1
while i <=  numero:
    suma += i
    i += 1
print ("La suma es de: ", suma)