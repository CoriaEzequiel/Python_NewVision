'''
Un hospital de Ciudad de la Habana necesita un programa para gestionar diariamente los datos de las diferentes salas de ingreso que dispone. 
El hospital dispone de salas de ingreso general y de salas de terapia.
De cada sala se controla el nombre por el cual se identifica y la cantidad de camas de que dispone. 
De las salas de ingreso se conoce además el nombre del médico que la atiende en ese día.
 De las salas de terapia se conoce, además de los datos generales para todas las salas, el estado general de los equipos de atención que puede ser bueno, regular o malo.

El hospital necesita conocer un indicador de calidad del trabajo de las salas.
Para las salas de ingreso, se halla determinando si la cantidad de pacientes ingresados es menor que la cantidad de camas y si existe el médico de guardia.
 Para el caso de las salas de terapia se determina si el estado de los equipos de atención es bueno.

El programa debe permitir:
a)	Cuántas salas tienen establecido el indicador de calidad.
b)	El listado de nombres de salas de terapia que tienen sus equipos de atención en mal estado.

1.	La aplicación debe tener un módulo dedicado a la programación y otro a la interfaz con el usuario.
2.	La clase controladora debe incluir una lista polimórfica, por lo tanto, se debe usar herencia, y métodos virtuales.
    Debe tener por lo menos un método que permita llenar la lista y métodos para la solución de los incisos planteados.
3.	La aplicación puede llenar los elementos de la lista con instancias creadas por el mismo programa.
    Puede también ser el resultado de entrada de datos del usuario, sin que sea obligatorio la validación de los datos ingresados.
'''