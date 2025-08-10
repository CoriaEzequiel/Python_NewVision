class Hotel:
    def __init__(self,nombre,ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):      #entrega objeto de la clase habitacion
        self.habitaciones.append(habitacion)
        print(f"Habitación {habitacion.numero} añadida al hotel {self.nombre}.")

    def eliminar_habitacion(self, habitacion):
        self.habitaciones.remove(habitacion)
        print(f"Habitacón {habitacion.numero} eliminada del hotel {self.nombre}.")
        
    def buscar_habitacion(self, tipo=None, precio_max=None):    #parametros, tipo o precio max, None por default. 
        resultados =[]                                          #asegurando evitar error que si no entrego algún parametro
        for habitacion in self.habitaciones:
            if(tipo is None or habitacion.tipo == tipo) and (precio_max is None or habitacion.precio <= precio_max):
               resultados.append(habitacion)
        return resultados
        
    def mostrar_info(self):
        return f"Hotel {self.nombre}, ubicado en {self.ubicacion}" 