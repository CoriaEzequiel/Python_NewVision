import numpy as np

#ubicar elemento mediante su posición.

m = np.arange(24).reshape(4,6)
print(m)
print(m [3,4])    #por fila y columna.
print(m)

w= np.array([777,144,222,9,45,2,5,1,101,7])
print(np.sort(w)) #ordeno mi matriz.

ma = np.array([2,3])
print(np.power(ma,3)) #cada elemento se eleva a x potencia.
print(np.array(ma**3))

mat = np.array([2,3,4,5,6,7])
print(np.array(mat>=4)) #devuelve True y False.

print(np.array(mat.max()))
print(np.array(mat.min()))


#combinar matrices
print(np.concatenate((w,mat)))

matr = np.array([[1,2],[3,4]])
matri = np.array([[5,6],[7,8]])

print(matr+matri)
print(matr +2)

#llamo  al módulo mp y mediante el punto llamo a la función:
print(np.add(matr,matri))
print(np.subtract(matr,matri))
print(np.multiply(matr,matri))
print(np.divide(matr,matri))


#.dot  según dimensiones de los arrays.

#Producto matriz 
print(matr.dot(matri))

#Producto punto
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

#forma moderna
print(a@b)
print(matr@matri)