from sistemareservas import SistemaReservas
from hotel import Hotel
from habitacion import Habitacion
from cliente import Cliente
from reserva import Reserva
#creo una instancia del sistema de reservas
sistema = SistemaReservas()

#creo algunos hoteles
hotel1 = Hotel("RosTower", "Rosario")
hotel2 = Hotel("City Center", "Rosario")
hotel3= Hotel("Patagonia", "Bariloche")


print(sistema.buscar_hoteles("Rosario")) #debo registrar primero

#Registro hoteles en el sistema
sistema.registrar_hotel(hotel1)
sistema.registrar_hotel(hotel2)
sistema.registrar_hotel(hotel3)

print(sistema.buscar_hoteles("Rosario"))

print(sistema.buscar_hoteles("Rosario")[0])

#Agrego habitaciones a los hoteles

habitacion1 = Habitacion(101, "simple", 100)
habitacion2 = Habitacion(102, "doble", 150)
habitacion3 = Habitacion(202, "suite", 300)

hotel1.agregar_habitacion(habitacion1)
hotel1.agregar_habitacion(habitacion2)
hotel2.agregar_habitacion(habitacion3)

print(hotel1.habitaciones) #enseña los objetos creados

#creo cliente
cliente1 = Cliente(1,"Coria Ezequiel","Ez@gmail.com")
cliente2= Cliente(2,"Axl Rose", "Axelito@gmail.com")

#registro cliente
sistema.registrar_cliente(cliente1)
sistema.registrar_cliente(cliente2)

#Cliente1 realiza una reserva
reserva1 = Reserva(1,habitacion1,cliente1, "2025-08-10", "2025-08-18")
print(reserva1.estado) #pendiente hasta que realiza reserva.
cliente1.realizar_reserva(reserva1)
print(reserva1.estado)


#Cliente2 realiza una reserva
reserva2 = Reserva(2, habitacion3, cliente2, "2026-01-05", "2026-01-29")
cliente2.realizar_reserva(reserva2)

sistema.listar_reservas()

#modifico una reserva
reserva1.modificar_reserva("2024-08-11", "2024-08-19")
sistema.listar_reservas()

#cancelo una reserva
reserva2.cancelar_reserva()

sistema.listar_reservas()

#Muestro información de los hoteles y habitaciones disponibles:
print("\nInformación de hoteles y habitaciones:")
for hotel in sistema.hoteles:
    print(hotel.mostrar_info())
    for habitacion in hotel.habitaciones:
        print(habitacion.mostrar_info())