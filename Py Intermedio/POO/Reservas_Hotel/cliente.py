class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email
        self.reservas = []

    def realizar_reserva(self,reserva):
        self.reservas.append(reserva)
        reserva.estado = "confirmada"
        print(f"""Reserva {reserva.id_reserva} realizada por {self.nombre} para la habitación {reserva.habitacion.numero}.""")

    def cancelar_reserva(self,reserva):
        if reserva in self.reservas:        #compruebo si la reserva está en la lista de reservas del cliente
            reserva.cancelar_reserva()
            self.reservas.remove(reserva)