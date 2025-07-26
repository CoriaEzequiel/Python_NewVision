class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular              #atributos de instancia.
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad} dolares. Su  saldo actual: U$D {self.saldo}")
        else:
            print("La cantidad debe ser mayor a 0.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("fondo insuficiente corazón.")
        elif cantidad <= 0:
            print("La cantidad debe ser mayor  a cero corazón de dinosaurio.")
        else:
            self.saldo -= cantidad  
            print(f"Se han retirado {cantidad} dolares. Su saldo actual U$D {self.saldo}")

    def obtener_saldo(self):
        return self.saldo
    

#uso

if __name__ == "__main__":
    cuenta = CuentaBancaria("Ez Coria", 1200)
    cuenta.depositar(1200)
    cuenta.retirar(500)
    print(f"Su saldo actual : U$D {cuenta.obtener_saldo()}")