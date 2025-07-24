#FUNCIONES COMO PARÁMETROS


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def aplicar_operacion (a,b, operacion):
    return operacion(a,b)

resultado_suma = aplicar_operacion(5,5, suma)
print("Resultado suma: ", resultado_suma)

resultado_resta = aplicar_operacion(10,5, resta)
print("Resultado resta: ", resultado_resta)

resultado_multiplicacion = aplicar_operacion(2,2,multiplicacion)
print("Resultado multiplicacón: ",resultado_multiplicacion)

def saludar(nombre):                    #Función sin retorno.
    mensaje= f"hola, {nombre}"
print(saludar("Amalia"))                #Devuelve None / (No retorna mensaje)


def saludar(nombre):
    mensaje= f"hola, {nombre}"
    return mensaje
print(saludar("Amalia"))


def dividir_y_resto(a,b):           #Función con múltiples retornos 
    division = a//b
    resto = a%b
    return division, resto          #devuelve una tupla

resultado_division, resultado_resto = dividir_y_resto(10,3)     #desempaquetado / unpacking para devolver resultados por separado   
print("el resultado de la division es : ", resultado_division)  #sino se debería usar índice para acceder a cada valor.
print("el resto de su division es: ", resultado_resto)
