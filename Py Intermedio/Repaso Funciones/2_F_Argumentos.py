#Python permite mezclar argumentos posicionales y nominales. pero los posicionales deben ir antes.

def imprimirInfo(nombre,edad,ciudad):
    print(f"Nombre: {nombre}") 
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")

imprimirInfo("Lu",22, ciudad="Rosario")

imprimirInfo("Ez", 30, "Rosario")

imprimirInfo("Mati", 20, "Santa fé")


#PARÁMETROS POR DEFECTO.

def calcular_area_rect (base= 1, altura= 1):
    area = base * altura
    return area

area1 = calcular_area_rect()
area2 = calcular_area_rect(5)
area3 = calcular_area_rect(3,4)

print(area1, area2, area3)


def multiplicar_dos_num():
    num1 = int(input("Ingrese num 1: "))
    num2 = int(input("Ingrese num 2: "))
    multi = num1 * num2
    return num1, num2, multi  # Devuelvo los tres

# Desempaqueto los valores retornados
n1, n2, resultado = multiplicar_dos_num()
print(f"El resultado de multiplicar {n1} * {n2} = {resultado}")



#Otra forma:

def multiplicar_dos_num(num1, num2):
    return num1 * num2

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

resultado = multiplicar_dos_num(n1, n2)

print(f"El resultado de multiplicar {n1} * {n2} es: {resultado}")



#------------------------------------------------------------------------------#

def concatenarStrings(*arg):    # arg permite recibir una cantidad variable de argumentos
    resultado=""                #inicializa string vacío
    for cadena in arg:          # en cada iteración la cadena irá tomando el nuevo valor.
        resultado+= cadena + " "
    return resultado.strip()

frase = concatenarStrings("Hola", "Encantadísimo de", "poder formar parte del equipo", "de desarrolladores.")
print(frase)




def sumar_valores(*arg):            #* recibe argumentos posicionales, se agrupan en tuplas
    total = sum(arg)
    return total

numeros_a_sumar =(10,20,30,40,50)
resultado= sumar_valores(*numeros_a_sumar)
print(resultado)

def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")
imprimir_datos(nombre="Emma", edad=24, ciudad = "Cordoba", pais = "Argentina")        

def imprimir_datos(**datos):
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")
imprimir_datos(nombre="Amalia", edad=26, ciudad ="Cordoba", pais ="Argentina")


def imprimir_datos_(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ciudad = input("Ingrese su ciudad: ")
pais = input("Ingrese su país: ")

datos_usuario = {
    "nombre": nombre,
    "edad": edad,
    "ciudad": ciudad,
    "pais": pais
}

imprimir_datos_(**datos_usuario)        #recibe argumentos nominales (clave/valor), se agrupan en diccionarios.



def calcular_precio(producto, precio_unitario, cantidad):
    total= precio_unitario * cantidad
    print(f"Producto:{producto}")
    print(f"Precio Unitario:{precio_unitario}")
    print(f"Cantidad:{cantidad}")
    print(f"Total:{total}")

datos_producto = {"producto":"camisa", "precio_unitario":35, "cantidad":1}
calcular_precio(**datos_producto)                                               #desempaqueta diccionario.