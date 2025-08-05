import itertools

datos = [
    {'ciudad': 'Rosario', 'temp': 22},
    {'ciudad': 'Mendoza', 'temp':24},
    {'ciudad': 'Rosario', 'temp': 20},
    {'ciudad': 'Mendoza', 'temp':26},
]

datos.sort(key=lambda x: x['ciudad'])

agrupados = itertools.groupby(          #recibe el iterable(lista de datos)
    datos,
    key=lambda x: x['ciudad']            #y una función que indica cómo agrupar los datos (según su clave )
)
#devuelve un iterador de tuplas (key, group_iterator)

for ciudad, grupo in agrupados:
    print(f"Ciudad: {ciudad}")
    for item in grupo:
        print(f" - {item['temp']}ºC")
