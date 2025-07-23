#Grupo de sentencias - Bloques de código que realizan una tarea concreta.
#Permite no repetir fragmentos de código y reutilizar  el código en distintos escenarios.
#A los fragmentos que no retornan valor se los llama "PROCEDIMIENTOS"
#PARÁMETROS : variables en la definición, van en la declaración de la función
#ARGUMENTOS: valores reales que se pasan entre paréntesis a la función cuando es invocada. 
#pass permite "no hacer nada"

#define
def suma(a,b,c):
    return(a+b+c)
                           
resultado = suma(1,2,3)             #llama función
print("El resultado es", resultado)


resultado2 =suma(int(input("Ingrese primer número: ")), int(input("Ingrese segundo número: ")), int(input("Ingrese tercer número: ")))  #llama función
print("La suma de sus numeros es de: ", resultado2)



numeros = [int(input("Ingrese primer número: ")),
           int(input("Ingrese segundo número: ")),
           int(input("Ingrese tercer número: "))]

resultado3= suma(*numeros) #llama función
print(f"La suma de sus números es de: ", resultado3)
print(f"Extraordinaria decisión de su segundo número {numeros[1]}")

#ARGUMENTOS POSICIONALES: se copian en sus correspondientes parámetros por orden de escritura
#ARGUMENTOS NOMINALES: NO son copiados en orden específico, se asignan por nombre

#funcion con argumentos nominales:

def saludar(nombre, saludo):
    print(f"{saludo}, {nombre}! Que tengas un excelente día!")

saludar (saludo= "Hola ", nombre="Anto")