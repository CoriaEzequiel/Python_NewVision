#Funciones predefinidas

#abs() Valor absoluto

num = -50
valor_absoluto = abs(num)
print(valor_absoluto)

def calcular_valor_ab(numero):
    return abs(numero)

num = float(input("Ingrese su número: "))
resultado = calcular_valor_ab(num)

print("El valor absoluto de su número es de: ", resultado)



def calcular_valor_ab(numero):
    return abs(numero)

num = float(input("Ingrese un número: "))
resultado = calcular_valor_ab(num)
print("el valor absoluto es :", resultado)


#max() Valor más grande
lista_numeros = [2,96,777,111,55,808,222, 1]
maximo = max(lista_numeros)
print(maximo)

#min()
min = min(lista_numeros)
print(min)

#sum()
suma_total = sum(lista_numeros)
print(suma_total)


#round() redondéa
num_decimal = 10.69
redondeo = round(num_decimal)
print("El numero redondeado es: ", redondeo)

#sorted() lista ordenada
mi_lista_ordenada = sorted(lista_numeros)
print("la lista ordenadita: ", mi_lista_ordenada)


#zip() 
primera_lista = [1,2,3,4,5]
segunda_lista = ["papa","calabazas", "zapallitos", "cebollas", "camotes"]

combi_zip = zip(primera_lista, segunda_lista)       #lazy iterator "listo para ser consumido"
lista_combinada = list(combi_zip)                   
print("listas combinadas", lista_combinada)


'''
primera_lista = [1,2,3,4,5]
segunda_lista = ["papa","calabazas", "zapallitos", "cebollas", "camotes"]

combi_zip = list(zip(primera_lista, segunda_lista))             
print("listas combinadas: ", combi_zip)

'''

#enumerate() retorna enumeración de un iterable, devuelve pares: índice y valor
frutas= ["Manzanas", "Uvas", "Peras","Bananas"]
enumeracion = list(enumerate(frutas))
print(enumeracion)


#any() MANEJA BOOL: devuelve True si al menos un elemento es verdadero.

valores =[True, False, True, False]
existe_verdadero = any(valores)
print("Existe?", existe_verdadero)


#all() devuelve True si TODOS los elementos son verdaderos.
all_valores = all(valores)

nuevos_valores = [True, True, True]
all_valores_ = all(nuevos_valores)
print("son todos true?", all_valores)
print("son todos true?", all_valores_)


#eval() evalua expresión 
resultado = eval("3+5")
print( resultado)

'''
Toma un string como argumento y lo interpreta como código de Python, ejecuta y devuelve resultado.
cálculos dinámicos, evalúa strings, evalúa condiciones lógicas, cualquier código incluso cosas "destructvias".
Cuidado con imports (no debería usarse con datos que vengan de usuarios o fuentes externas).
'''

#filter() aplica una función a cada elemento de un iterable y devuelve un iterador de solo los que dan True


def es_par(numero):
    return numero % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
pares= list(filter(es_par,numeros))
print("Numeros pares:",pares)


#map() aplica función a cada elemento de un iterable y retorna un iterador con los resultados. (quen en este caso lo transformamos en lista)

def  duplicar(numero):
    return numero*2

resultado_duplicado = list(map(duplicar, numeros))
print("El resultado de los números duplicados: ",resultado_duplicado)


#reversed() invierte una secuencia.
palabra = "Python"
reverso =  reversed(palabra)
print(''.join(reverso))         #une elementos del iterable en un solo string


#slice()
secuencia = [1,2,3,4,5,6,7,8,9]
porcion = slice(2,5)
print("slice: ", secuencia[porcion])


#chr()

codigo_unicode = 65
caracter = chr(codigo_unicode)
print("el código a char", caracter)
print(type(caracter))

#ord()
caracter = 'C'
codigo_unicode = ord(caracter)
print(codigo_unicode)


#bin()
numerito = 6
binario = bin(numerito)
print (f"el número {numerito} en binario es:", binario)

#octal()
octal = oct(numerito)
print (f"el número {numerito} en octal es:", octal)

#hex()
hexadecimal = hex(numerito)

print (f"el número {numerito} en hexadecimal es:", hexadecimal)

#exec()
codigo = "print('Hola Mundo')"
exec(codigo)