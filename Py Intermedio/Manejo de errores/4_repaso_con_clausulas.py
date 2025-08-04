try:
    x = int(input("Ingrese un número: "))
    resultado = 10/x

except ZeroDivisionError:
    print("Error belleza de Dios, no puede dividir por cero.")
except ValueError:
    print("Error corazón de pajarito, debe ingresar un número entero.")
except Exception as ex:
    print(f"Vaya vaya, ha sucedido un Error inesperado: {ex}")

else: print(f"El resultado de dividir 10 por el número: {x} es {resultado} ")

finally: print("Vuelva pronto!")