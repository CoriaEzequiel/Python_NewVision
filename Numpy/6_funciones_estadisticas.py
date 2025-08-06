import numpy as np

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(m)
print("\n")
print(np.amax(m))   #Devuelve el valor máximo total de la matri
print(np.amin(m))   #Devuelve el valor mínimo total de la matriz
print(np.amax(m,1)) #máximo de cada fila
print(np.amax(m,0)) #máximo de cada columna
print(np.amin(m,1)) #mínimo de cada fila
print(np.amin(m,0)) #mínimo de cada columna


#Rango = Max(x) - min(x)
print(np.ptp(m))
print(np.ptp(m, axis=1))
print(np.ptp(m,axis =0))

# Percentil: valor para comparar un conjunto (en este caso ordenado de datos)
# (q(n+1))/100
# Esta fórmula solo funciona cunado los elementos de la matriz son impares(n impar).
print(np.percentile(m,50))
print(np.percentile(m,50, axis=1)) #valor únicamente para filas
print(np.percentile(m,50, axis=0)) #valor únicamente para columnas

# Mediana = (n+1)/2
print(np.median(m))
print(np.median(m, axis=0))
print(np.median(m, axis=1))

# Media aritmética = (x1+x1+xn) / n
print(np.mean(m))
print(np.mean(m, axis=0))
print(np.mean(m, axis=1))

# Promedio ponderado

a = np.array([1,2,3,4,5,6])
print(a)
print("\n")
print(np.average(a))

# Desviación estándar
# std = sqrt(mean(abs(x-x.mean())**2))
print(np.std(a))