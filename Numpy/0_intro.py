'''
Simplifico la estructura 

import array as ar
matriz = ar.array('i',[1,2,3,4,5])      #Almaceno información dentro de la estructura matriz
print(matriz)

for ar in matriz:
    print(ar)
    
'''
import numpy as np
matriz = np.array([1,2,3,4,5])
print(matriz)


lista  = [1,3,5]
matriz = np.array([2,4,6])

lista.append(7) 
# matriz.append(8) ESTO NO ES POSIBLE
matriz = matriz + np.array([8]) #este valor se agrega de manere indiviual a cada elemento del array.

print(lista)        #las listas se separan por comas, es una colección de elementos.
print(matriz)       #también es una estructura, pero cada elemento es independiente.
                    #ocupando un determinado espacio de memoria.

#LAS LISTAS NO PUEDEN MANEJAR OPERACIONES ARITMÉTICAS DE MANERA DIRECTA
#Array si es posible manejar directamente las operaciones aritméticas.

a = [1,2,3]
b = [4,5,6]

print(a+b) #IMPRIME UNA SUMA DE LISTAS
# print(a*b) NO ES POSIBLE.

#contrario a las matrices:

am = np.array([1,2,3])
bm = np.array([4,5,6])

print(am+bm)
print(am*bm)

#si voy a tener muchos elementos dentro de una estructura es conveniente utilizar Array.
#pocos elementos: Listas.

#Arrays, comparativamente más compacto en tamaño de memoria 
#Listas, consume más memoria para agregar elementos fácilmente 

#los Arrays se consideran vectores: tienen un inicio, un cuerpo y un final.
#Siempre está ordenado de manera interna.
#para las listas utilizamos punteros.