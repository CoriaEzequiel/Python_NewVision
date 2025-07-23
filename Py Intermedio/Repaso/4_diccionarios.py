# Diccionarios : almacenan conjuntos de elementos. Pares de elementos clave/valor

diccionario1 = {
              "Nombre": "Ezequiel",
              "Edad": 30,
              "Ciudad": "Rosario",
              "Deporte Favorito": "Taekwondo"
}

print(diccionario1["Deporte Favorito"])


#otra manera de crear diccionario / Método dict

diccionario2 = dict([
              ('Nombre', 'Sara'),
              ('Edad',29),
              ('Ciudad', 'Buenos Aires'),
              ('Deporte Favorito', 'Voley')
])

print(diccionario2)


dicconario3 = dict(Nombre="Clara", Edad="26", Ciudad="La plata", Deporte_Favorito = "Danzas")

print(dicconario3)

#Acceder a un elemento de forma tradicional
print(diccionario1["Edad"])

#Acceder a un elemento /Método get()

print(diccionario1.get("Nombre"))

# Actualizar
diccionario2["Edad"] = 32
print (diccionario2)

#Añadir elemento CLAVE/VALOR
dicconario3["Pais"] = "Argentina"

print(dicconario3)

#iterar diccionario /Desplegar

for i in dicconario3:               #itera solo las claves
    print(i)

for s in diccionario1:              #itera solo los valores
    print(diccionario1[s])

for x,y in diccionario2.items():        #itera claves y valores
    print(x,y)


#Consultas de Diccionarios / Método get()
print(diccionario1.get("Deporte Favorito"))

#Método items()
print(diccionario1.items())

#Método keys()
print(diccionario1.keys())

# Método values()
print(diccionario1.values())


dicconario3.popitem()   #Método eliminar el último.
print(dicconario3)

dicconario3.pop('Edad') 
print(dicconario3)
