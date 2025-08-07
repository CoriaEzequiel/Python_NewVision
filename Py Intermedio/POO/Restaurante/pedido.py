class Pedido:
    def __init__(self, numero: int, items: list, preparado: bool = False):
        self.numero = numero
        self.items = items
        self.preparado = preparado

    def total(self):
        return sum(item.precio for item in self.items)

    def esta_listo(self):
        return self.preparado

    def preparar(self):
        self.preparado = True

    def __str__(self):
        estado = "Listo" if self.preparado else "Pendiente"
        items_str = "\n  ".join(str(item) for item in self.items)
        return f"Pedido #{self.numero} - {estado}\n  {items_str}\n  Total: ${self.total():.2f}"