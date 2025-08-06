#print(m.shape) #función que devuelve cantidad de filas y columnas
#print(m.ndim)  #función que devuelve cantidad de dimensiones
#print(m.size)  #función que devuelve cantidad de elemnetos que posée mi matriz

import numpy as np
m = np.zeros((3,4))
print(m.size)
print(m)

w= np.arange(10)
print(w.size)
print(w)

#función linspace: 
#(primer elemento de la matriz, valor posicionado en el último elemento y cuántos elementos quiero ver)
#genera un array de números espaciados de forma uniforme  entre dos valores.
#crea rangos de valores continuos.
#se utiliza mucho en gráficos y simulaciones matemáticas donde se necseita puntos intermedios

lp = np.linspace(99,88,25)
print(lp.size)
print(lp)

lin = np.linspace(0,1,5)
print(lin)


#matrices 3D con arange.
#(cantidad de matrices, filas y columnas)
m3d = np.arange(24).reshape(2,3,4)
print(m3d)

w3d = np.arange(27).reshape(3,3,3)
print(w3d)
