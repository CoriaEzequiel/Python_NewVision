class Restaurante:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def pedidos_listos(self):
        return [p for p in self.pedidos if p.esta_listo()]

    def pedidos_pendientes(self):
        return [p for p in self.pedidos if not p.esta_listo()]

    def preparar_pedido(self, numero):
        for pedido in self.pedidos:
            if pedido.numero == numero:
                pedido.preparar()
                return True
        return False

    def mostrar_todos_los_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)
            print("-" * 40)