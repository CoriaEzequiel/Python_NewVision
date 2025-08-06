#el objetivo de estos números aleatorios no es que sea diferente cada vez
# sino que no se pueda predecir lógicamente (con exactitud)
import numpy as np

m = np.random.randint(10, size=(5))
print(m)

w= np.random.randint(10, size=(3,3))    #dimensión de matriz
print(w)

ma= np.random.rand(5)   #números con decimales
print(ma)


#matriz de dos dimensiones con números decimales
wa = np.random.rand(2,2)
print(wa)

#función para devolver 1 solo valor de una matriz
mat = np.random.choice([5,6,4,3,7,8,1])
print(mat) 

#matriz en 2D
#primer argumento: lista de elementos a elegir
#segundo argumento: keyword argument
mat2d = np.random.choice ([3,5,7,8,0,9], size =(2,3))
print(mat2d)


#Distribución Aleatoria:

# Es una lista de todos los valores posibles 
# y la frecuencia con la que se produce cada valor.

# Conjunto de números aleatorios
# que siguen una determinada función de densidad y de probabilidad

#(matriz de valores,matriz de probabilidad y tamaño)
a = np.random.choice\
    ([2,4,6], p = [0.3,0.3,0.4], size=(15))
print(a)

b = np.random.choice\
    ([1,2,3,4,5,6], p = [1/6,1/6,1/6,1/6,1/6,1/6], size=(15))
print(b)

c = np.random.choice\
    ([2,4,8,10,5], p = [0.3,0.2,0.1,0.2,0.2], size=(20))
print(c)