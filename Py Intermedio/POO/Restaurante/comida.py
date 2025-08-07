from item import Item

class Comida(Item):
    def __init__(self, nombre: str, precio: float, vegetariana: bool = False):
        super().__init__(nombre, precio)
        self.vegetariana = vegetariana

    def __str__(self):
        tipo = "Vegetariana" if self.vegetariana else "No vegetariana"
        return f"{self.nombre} ({tipo}) - ${self.precio:.2f}"