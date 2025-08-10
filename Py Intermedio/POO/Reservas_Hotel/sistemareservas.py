class SistemaReservas:
    def __init__(self):
        self.hoteles = []
        self.clientes = []

    def registrar_hotel(self,hotel):
        self.hoteles.append(hotel)
        print(f"Hotel {hotel.nombre} registrado en el sistema.")

    def eliminar_hotel(self,hotel):
        self.hoteles.remove(hotel)
        print(f"Hotel {hotel.nombre} eliminado del sistema.")

    def registrar_cliente(self,cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} registrado con éxito.")

    def eliminar_cliente(self,cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} eliminado del sistema.")

    def buscar_hoteles(self, ubicacion=None, nombre=None):  #busco hotel por ubicacion o por nombre
        resultados=[]
        for hotel in self.hoteles:
            if (ubicacion is None or hotel.ubicacion == ubicacion ) and (nombre is None or hotel.nombre == nombre):
                resultados.append(hotel)
        return resultados
    

    def listar_reservas(self):          #recorro cada clientes y cada reserva del cliente
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                print(f"""Reserva {reserva.id_reserva} para el cliente {cliente.nombre},
                      para la fecha comprendida desde {reserva.fecha_entrada}, hasta {reserva.fecha_salida}
                      Estado: {reserva.estado}. """)