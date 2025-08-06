import numpy as np
m = np.array([[1,-1,2], [3,2,0]])
print(m)
print("\n")

m1 = np.array([[1],[2],[3]])
print(m1)

# Matriz traspuesta
# se obtiene cambinado filas por columnas (o viceversa).

print(np.transpose(m1))
print(np.transpose(m))

w = np.array([[1,2,3]]) #es importante mantener la forma englobando toda la matriz.
print(np.transpose(w))

#Resolución de sistemas de ecuaciones lineales

A= np.array([[2,1,-2],[3,0,1],[1,1,-1]]) #Matriz original
b= np.array([[-3],[5],[-2]])             #Términos independientes

print(A)
print("\n")
print(np.transpose(b))
print("\n")
#utilizando Función solve para resolver sistemas, del submódulo linalg de la librería NumPy  
x = np.linalg.solve(A,b)
print(x)

print(np.allclose(np.dot(A, x) ,b)) #Verifico si el resultado es correcto


#Sistema de ecuaciones.
# 2x + 7y + 3z = 1
# 2x + 8y + 2z = 1
#  x + 3y +  z = 0

mtr1= np.array([[2,7,3], [2,8,2],[1,3,1]])
print(mtr1)

mtr2 = np.array([1,1,0])
#otra manera de transponer automaticamente.
#3 filas y 1 sola columna:
mtr2.shape=(3,1)
print(mtr2)

print("\n")
print(np.linalg.solve(mtr1,mtr2))
