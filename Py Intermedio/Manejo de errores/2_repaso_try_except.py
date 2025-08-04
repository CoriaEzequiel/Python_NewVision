try:                            #Encierro un bloque de código que no estoy seguro si va a funcionar
    resultado = 10/0            #Solo se ejecuta dentro del try, sin afectar las demás lineas de código.
except ZeroDivisionError as e:
    print(f"Error papacito: {e}")

try:
    print(spam)
except NameError as e:
    print(f"Error papacito:{e}")

try:
    resultado = '2' + 2
except TypeError as e:
    print(f"Error papacito:{e}")

try:
    x=10/0
except ZeroDivisionError as e:
    print("No se puede dividir por 0 papacito")