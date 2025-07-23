#solo tiene métodos Contar y Buscar

tupla = (1,2,3)
print(tupla)

lista = ['a','b','c']
tuplita = tuple(lista)
print(lista)
print(tuplita)

#iteración en tupla
for i in tuplita:
    print(i)

#desempaquetar tupla

one, two, three = tuplita
print(two)    

lechuguita, tomatito, rabanito = tupla
print(rabanito)

#contar elementos repetidos dentro de una tupla / Método Count()
nueva_tuplita = (1,2,3,3,4,5,5,5,5)
print(nueva_tuplita.count(5))

# método index() / índice de primera vez que aparece el elemento.
print(nueva_tuplita.index(2))