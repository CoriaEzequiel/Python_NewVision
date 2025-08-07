from comida import Comida
from bebida import Bebida
from bebida_alcoholica import BebidaAlcoholica
from pedido import Pedido
from restaurante import Restaurante

# Creo restaurante (controlador principal)
restaurante = Restaurante()

# Creo los productos
pizza = Comida("Pizza Margarita", 1200, vegetariana=True)
hamburguesa = Comida("Hamburguesa doble", 1800, vegetariana=False)
cafe = Bebida("Café", 500, fria=False)
gaseosa = Bebida("Gaseosa cola", 600)
cerveza = BebidaAlcoholica("Cerveza artesanal", 900, grados_alcohol=5.4)

# Crear pedidos
pedido1 = Pedido(1, [pizza, gaseosa])
pedido2 = Pedido(2, [hamburguesa, cerveza])
pedido3 = Pedido(3, [cafe, pizza, gaseosa])

# Agrego pedidos al restaurante
restaurante.agregar_pedido(pedido1)
restaurante.agregar_pedido(pedido2)
restaurante.agregar_pedido(pedido3)

# Preparo algunos pedidos
restaurante.preparar_pedido(1)
restaurante.preparar_pedido(3)

# Enseño pedidos listos
print("Pedidos listos:")
for pedido in restaurante.pedidos_listos():
    print(pedido)
    print("-" * 40)

# Enseño pedidos pendientes
print("\n Pedidos pendientes:")
for pedido in restaurante.pedidos_pendientes():
    print(pedido)
    print("-" * 40)

# Enseño todos los pedidos
print("\n Todos los pedidos:")
restaurante.mostrar_todos_los_pedidos()