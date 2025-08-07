from item import Item

class Bebida(Item):
    def __init__(self, nombre: str, precio: float, fria: bool = True):
        super().__init__(nombre, precio)
        self.fria = fria

    def __str__(self):
        temperatura = "Fría" if self.fria else "Caliente"
        return f"{self.nombre} ({temperatura}) - ${self.precio:.2f}"