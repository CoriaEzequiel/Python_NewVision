#extraer elementos de una lista   "Desempaquetar Lista"

numeros = [1,2,3,4,5]

primero, segundo, tercero, cuarto, quinto = numeros
print(cuarto)

#Buscar por index / Método buscar

listaLenguajes = ['Python','Ruby','C++','JavaScript','Assembler','Java']
indice = listaLenguajes.index('C++')
print(indice)

#Recorrer una lista / Método for : desplega lista

for lenguaje in listaLenguajes:
    print(lenguaje)


#Recorrer lista / Método enumerate : desplega lista e indica índice, posición.

for lenguaje in enumerate(listaLenguajes):
    print(lenguaje)

for i, lenguaje in enumerate(listaLenguajes):
    print(i, lenguaje)