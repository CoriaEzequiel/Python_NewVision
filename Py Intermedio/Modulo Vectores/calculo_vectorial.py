import math

#módulo para leer cada vector ingresado
def leer_vector():
    entrada = input("Introducir componentes del vector, separados por comas: ")
    return list(map(float, entrada.split(',')))

def mostrar_vector(v): #ingresa una lista y la enseño.
    print(f"Vector: {v}")

def misma_dimension(v1,v2): #compara si los vectores son de misma dimensión    
    return len(v1) == len(v2)

#suma de vectores

def suma_vectores(v1,v2): #necesito los datos de vector 1 y el vector 2
    if not misma_dimension(v1,v2):
        raise ValueError("Los vectores no tienen la misma dimensión.")
    return [a + b for a,b in zip(v1,v2)]

#resta de vectores

def resta_vectores(v1,v2):
    if not misma_dimension(v1,v2): 
        raise ValueError("Los vectores no tienen la misma longitud.")
    return [a - b for a,b in zip(v1,v2)]

#modulo del vector
def modulo_vector(v):
   return math.sqrt(sum([x**2 for x in v]))

#modulo producto punto
def producto_punto(v1,v2):
    if not misma_dimension(v1,v2):
        raise ValueError("Los vectores no son de la misma dimensión.")
    return sum(a*b for a,b in zip(v1,v2))


#verifica si los vectores son perpendiculares

def vectores_perpendiculares(v1,v2):
    return producto_punto(v1,v2) == 0

#producto escalar 
def producto_escalar(k,v):
    return [k * x for x in v]

#producto cruz
def producto_cruz(v1,v2):
    if len(v1) != 3 or len(v2) != 3:
        raise ValueError("El producto cruz solo está definido para vectores en R3")
    a1, a2, a3 = v1
    b1, b2, b3 = v2
    return[a2*b3 - a3*b2,
           a3*b1 - a1*b3,
           a1*b2 - a2*b1]