import numpy as np
m2d = np.array([[1,2,3],[4,5,6]]) #matriz 2d
print(m2d)

lista = [1,2,3,4,5,6]       #lista a matriz
matriz = np.array(lista)
print(matriz)


lista_de_filas = [[[1,2,3],[4,5,6],[7,8,9]]] #matriz 3d
matriz_3x3 = np.array(lista_de_filas)
print(matriz_3x3)

m = np.arange(15).reshape(3,5)   #valores para filas y columnas
print(m)

w = np.arange(30).reshape(3,10) # debe cumplir con la cantidad de elementos que requiere la matriz.
print(w)

print(m.shape) #función que devuelve cantidad de filas y columnas
print(m.ndim)  #función que devuelve cantidad de dimensiones
print(m.size)  #función que devuelve cantidad de elemnetos que posée mi matriz

