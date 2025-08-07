from bebida import Bebida

class BebidaAlcoholica(Bebida):
    def __init__(self, nombre: str, precio: float, grados_alcohol: float):
        super().__init__(nombre, precio, fria=True)
        self.grados_alcohol = grados_alcohol

    def __str__(self):
        return f"{self.nombre} (Alcohol {self.grados_alcohol}%) - ${self.precio:.2f}"