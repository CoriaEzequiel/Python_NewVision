#Modulo datetime

from datetime import datetime
import os

#función today() Objeto tipo DateTime que representa fecha y hora actual.

ahora = datetime.today()
print("el día y la hora actual es: ", ahora)


#Función strftime   "ejemplo: formato arg."

fecha_formato = ahora.strftime('%d-%m-%Y %H:%M:%S')
print("la hora formateada: ", fecha_formato)

#Función strptime(s, format) Maneja 2 atributos.
fecha_str = '2025-07-13'
fecha_objeto = datetime.strptime(fecha_str, '%Y-%m-%d')
print(fecha_objeto)
fech_form = fecha_objeto.strftime('%d-%m-%Y')
print("formateado queda", fech_form)


#Modulo OS / método  os.getcwd()

directorio_actual = os.getcwd()
print("El directorio actual es: ", directorio_actual)

#mkdir (path)
#listdir(path)
#remove(path)

#archivos_directorio = os.listdir('c:/Users')
#print(archivos_directorio)


