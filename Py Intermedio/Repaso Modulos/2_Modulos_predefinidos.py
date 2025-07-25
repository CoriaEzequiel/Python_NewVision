#Módulo math

#funcion sqrt(x)

import math
import random

num = 16
raiz = math.sqrt(num)
print( raiz)

#función pow(x,y)
base = 2
exponente = 3
resultado = math.pow(base, exponente)
print(resultado)

#funcion sin(x), cos(x), tan(x)
angulo_radian = math.radians (90)
seno = math.sin(angulo_radian)
coseno = math.cos(angulo_radian)
tangente = math.tan(angulo_radian)
print(seno, coseno, tangente)

#función exp()
exponencial = math.exp(1)
print(exponencial)

#factorial()
numero = 5
factorial = math.factorial(numero)
print(f"El factorial de {numero} es de:", factorial)

#log(x, base) tambien requiere dos parámetros

numerito = 100
base = 10
logaritmo = math.log(numerito,base)
print(f"el logaritmo de {numerito} en base {base} es: ", logaritmo)

#Modulo random

                     #(llamo mod, llamo funcion)
numero_aleatorio = random.random()
print("número random: ", numero_aleatorio)

#randint(x,y)
otro_numero_aleatorio = random.randint(1,300)
print("Numero aleatorio entero:", otro_numero_aleatorio)


#choice(secuencia) / Selecciona un elemento aleatorio
lista = ['a','b','c','d','e']
elemento_aleatorio_de_mi_ista = random.choice(lista)
print(elemento_aleatorio_de_mi_ista)


#shuffle(secuencia) / Mezcla elementos de la lista
random.shuffle(lista)
print(lista)

#sample(secuencia, k) / Muestra aleatoria de una secuencia
muestra_aleatoria = random.sample(lista, 2)
print("mira esta muestra aleatoria: ", muestra_aleatoria)