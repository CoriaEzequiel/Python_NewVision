#Elementos únicos, desordenados e inmutables. 

conjunto1 ={1,2,3,4,5,6}

#Método add()
conjunto1.add(7)
print(conjunto1)

#Método remove()
conjunto1.remove(4)
print(conjunto1)

#Método discard()
conjunto1.discard(3)
print(conjunto1)

#Método clear
#conjunto1.clear()
#print(conjunto1)

conjunto_a = {1,2,3,4,5,6,7}
conjunto_b = {2,6,7,8,9}

union = conjunto_a.union(conjunto_b)
print("La unión de ambos conjuntos:")
print(union)


interseccion = conjunto_a.intersection(conjunto_b)
print("La intersección de ambos conjuntos:")
print(interseccion)


diferencia = conjunto_a.difference(conjunto_b)
print("La diferencia desde conjunto A")
print(diferencia)

other_diference = conjunto_b.difference(conjunto_a)
print("La diferencia desde conjunto B")
print(other_diference)

#Diferencia simétrica. ENSEÑA LOS ELEMENTOS QUE NO SE REPLICAN EN AMBOS CONJUNTOS

simetrica = conjunto_a.symmetric_difference(conjunto_b)
print("simetrica")
print(simetrica)


disjunto = conjunto_a.isdisjoint(conjunto_b)
print("disjunto")
print (disjunto)

conjunto_one = {1,2,3}
conjunto_two = {7,4,5}
simetric = conjunto_one.isdisjoint(conjunto_two)
print ("NO TIENEN ELEMENTOS EN COMUN")
print(simetric)

#issubset() issuperset()