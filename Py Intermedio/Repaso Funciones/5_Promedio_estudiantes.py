def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

promedios = {}

num_estudiantes = int(input("¿Cuántos estudiantes desea ingresar? "))

for i in range(num_estudiantes):
    nombre = input(f"\nIngrese nombre del estudiante {i+1}: ")
    calificaciones_input = input(f"Ingrese las calificaciones de {nombre}, separadas por espacios: ")
    calificaciones = [int(x) for x in calificaciones_input.split()]
    promedio_actual = calcular_promedio(calificaciones)
    promedios[nombre] = promedio_actual

mejor_estudiante = max(promedios, key=promedios.get)
mejor_promedio = promedios[mejor_estudiante]

promedios_ordenados = dict(sorted(promedios.items(), key=lambda item: item[1], reverse=True))

print("\nPromedio de todos los estudiantes:")
for nombre, promedio in promedios.items():
    print(f"{nombre}: {promedio:.2f}")

print(f"\nEl estudiante con el mejor promedio es {mejor_estudiante}, con un promedio de {mejor_promedio:.2f}")

print("\nPromedios ordenados de mayor a menor:")
for nombre, promedio in promedios_ordenados.items():
    print(f"{nombre}: {promedio:.2f}")
