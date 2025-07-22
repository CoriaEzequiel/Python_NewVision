'''
Calcular IMC e interpretarlo
'''

peso = float(input("Ingrese su peso actual: "))
altura = float(input("Ingrese su altura actual: "))
imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print('Peso bajo')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc< 35:
    print('Obesidad grado I')
elif imc <40:
    print('Obesidad grado II')
else:
    print('Obesidad grado III')