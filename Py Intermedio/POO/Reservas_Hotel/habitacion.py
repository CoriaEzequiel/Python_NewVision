class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero        #atributos de la habitación generados en el constructor
        self.tipo = tipo
        self.precio = precio
        self.disponible = True

    def actualizar_disponibilidad(self, disponible):    #entrega parámetros de disponibildad 
        self.disponible = disponible                    #actualiza
        estado = "disponible" if disponible else "no disponible"
        print(f"habitación {self.numero} ahora está {estado}")

    def mostrar_info(self):
        return f"Habitación: {self.numero}, Tipo: {self.tipo}, Precio: ${self.precio} por noche"