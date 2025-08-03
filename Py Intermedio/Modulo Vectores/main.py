import calculo_vectorial as cv

v1 = [1,2,3]
v2=[4,5,6]

print("Suma:", cv.suma_vectores(v1,v2))
print("Resta:", cv.resta_vectores(v1,v2))
print("Módulo de v1:", cv.modulo_vector(v1))
print("Producto Punto de Vectores:", cv.producto_punto(v1,v2))
print("Son Perpendiculares?", cv.vectores_perpendiculares(v1,v2))
print("Resultado del Producto x Escalar:", cv.producto_escalar(2, v1))
print("Resultado del Producto Cruz:", cv.producto_cruz(v1,v2))