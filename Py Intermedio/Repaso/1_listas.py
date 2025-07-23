listaLenguajes = ['Python','Ruby','C++','JavaScript','Assembler','Java']

print(listaLenguajes[5])
print(listaLenguajes[:5])

#modificar lista
listaLenguajes[4] = 'C#'
print(listaLenguajes)

#agregar elemento / Métodos  append / por defecto se agrega al final.

listaLenguajes.append('Ross')
print(listaLenguajes)

#agregar elemento / Método insert  / maneja dos elementos: posición y elemento.

listaLenguajes.insert(1,'Go')
print(listaLenguajes)

#eliminar elemento de una lista / Método pop / Elimina último elemento
listaLenguajes.pop()
print(listaLenguajes)

#eliminar elemento que deseo / Método pop indicando índice.
listaLenguajes.pop(2)
print(listaLenguajes)

#eliminar elemento por nombre / Método remove.
listaLenguajes.remove('JavaScript')
print(listaLenguajes)

#eliminar / Método delete indicando índice.
del listaLenguajes[0]
print(listaLenguajes)

#eliminar / Método delete usando rangos.
del listaLenguajes[1:3]
print(listaLenguajes)

#eliminar / Método delete : elimina toda la lista.
del listaLenguajes

