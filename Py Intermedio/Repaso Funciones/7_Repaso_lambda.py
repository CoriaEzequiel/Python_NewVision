productos = [("Manzana", 30), ("Banana", 25), ("Naranja", 50), ("Sandía", 40)]

ordenados = sorted(productos, key=lambda item: item[1], reverse=True) #sorted  devuelve una nueva lista (no modifica la original)
                                                                      #key es una especie de filtro.
print("Productos ordenados por precio:")
for nombre, precio in ordenados:                                        #desempaquetamos variables de la tupla
    print(f"{nombre} - ${precio}")



#Ranking de empleados por productividad

empleados ={
    "Lourdes": [5,6,4,2,8],
    "Luana": [1,3,9,8,10],
    "Keyla": [4,5,7,9,8]
}

promedio = {nombre: sum(tareas )/len(tareas) for nombre, tareas in empleados.items()} #.items() obtengo lista iterable de pares clave/valor

promedios_ordenados = sorted(promedio.items(), key = lambda item: item[1], reverse=True)

print ("Ranking de productividad:")
for nombre, promedio in promedios_ordenados:
    print(f"{nombre}:{promedio:.0f} tareas por semana")


mejor_empleado = promedios_ordenados[0]
print (f"\n Empleado más productivo: {mejor_empleado[0]} con {mejor_empleado[1]:.0f} tareas semanales")


catalogo =[
    {"nombre": "Notebook", "precio":1500, "categoria":"Tecnología"},
    {"nombre": "Auriculares", "precio":100, "categoria":"Tecnología"},
    {"nombre":"Cafetera", "precio": 350, "categoria":"Hogar"},
    {"nombre":"Mesa", "precio": 600, "categoria": "Muebles"}
]

#filtro por categoríra "Tecnología"
tecnologia = [prod for prod in catalogo if prod["categoria"] == "Tecnología"]

#ordeno por precio ascendente
ordenadito = sorted(tecnologia, key= lambda item: item["precio"])

print("\n Su lista ordenadita: ")
for p in ordenadito:
    print(f"{p['nombre']} - ${p['precio']}")



#ANÁLISIS DE ARCHIVOS CON FECHAS

from datetime import datetime

archivos =[
    {"nombre": "informe.pdf", "taman":2.5, "fecha": "2024-05-20"},
    {"nombre":"respaldo.zip","taman":150, "fecha":"2024-05-18"},
    {"nombre":"foto.jpg", "taman":4.1,"fecha":"2025-01-12"},
    {"nombre":"video.mp4","taman":200, "fecha":"2025-06-21"}

]


# archivo: variable temporal que apunta a cada diccionario en la lista (para cada vuelta del for)
for archivo in archivos:
    archivo["fecha_obj"] = datetime.strptime(archivo["fecha"],"%Y-%m-%d") #convierto fechas a objetos "Datetime" para poder ordenarlos

#ordeno 
orden_por_fecha = sorted(archivos, key= lambda a: a["fecha_obj"], reverse=True)

print("Archivos ordenados por fecha: ")
for a in orden_por_fecha:
    print(f"{a['nombre']} - {a['fecha']}, {a['taman']} MB")


liviano = min(archivos, key= lambda a: a['taman'])
pesado = max(archivos, key= lambda a: a['taman'])

print(f"\n Archivo más liviano: {liviano['nombre']}, siendo de  {liviano['taman']}MB")
print (f"\n Archivo más pesado: {pesado['nombre']}, siendo de {pesado['taman']} MB  ")