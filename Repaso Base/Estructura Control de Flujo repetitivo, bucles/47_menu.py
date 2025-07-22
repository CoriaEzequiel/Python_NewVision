'''
Menú de opciones con opción de Salir del programa.
'''

while True:
    print("1 - Opción 1")
    print("2 - Opción 2 ")
    print("3 - Salir ")
    
    opcion = int(input("Elija una opción: "))

    if opcion == 1 :
        print('Usted a seleccionado la opción 1')
    elif opcion == 2 :
        print('Usted a seleccionado la opción 2')
    elif opcion == 3 :
        print('Hasta pronto')
        break
    else:
        print('No es una opción válida')