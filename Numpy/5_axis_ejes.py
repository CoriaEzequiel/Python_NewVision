# Manipulación de Ejes
# Tomando en cuenta coordenadas X axis e Y axis 
# Indicando direcciones Horizontal y vertical
# Útiles para encontrar un punto determinado en el espacio


#identifico con axis 1 para los elementos tomados en cuenta de manera horizontal: MIS FILAS (A1)
#identifico con axis 0 para los elementos tomados en ceunta de manera vertical: MIS COLUMNAS(A0)

# los Axis controlan los parámetros para cada función.

import numpy as np

m = np.array([[0,1,2],[4,2,3]])


print(m)
print("\n")
print(np.sum(m, axis=0)) #determina la dirección 0, a la función suma
print(np.sum(m,axis=1))#determina la dirección 1, a la función suma


a = np.array([[1,1],[1,1]])
b = np.array([[8,8],[8,8]])
print("\n")
print(a)
print("\n")
print(b)
print("\n")
print(np.concatenate([a,b], axis=0))
print("\n")
print(np.concatenate([a,b], axis=1))
print("\n")

# (Por obvias razones para matrices unidimensionales solo es posible axis con dirección en 0)
