class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depositó: U$D {cantidad}. Su saldo actual es de U$D {self.saldo}")
        else:
            print("Cantidad inválida para depositar.")

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print ("Fondos insuficientes.")
        elif cantidad <= 0:
            print("Cantidad inválida para retirar.")
        else:
            self.saldo -= cantidad
            print(f"usted retiró U$D {cantidad}. Su saldo actual es de U$D {self.saldo}")

    def obtener_saldo(self):
        return self.saldo
    
#SubClase para Cuenta de Ahorro     -> hereda todos los atributos (titular, saldo) y todos los métodos(depositar, retirar, obtener_saldo)

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, tasa_interes=0.02):        #agrega nuevo atributo. super() para heredar todo. no debemos volverlo a definir los atrib heredadores salvo que quiera modificarlo.
        super().__init__(titular,saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        print(f"Interés aplicado: U$D {interes}. Nuevo saldo: U$D {self.saldo}")


#SubClase para Cuenta Corriente
class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite_descubierto=500):       #agrego atributo nuevo
        super().__init__(titular, saldo)
        self.limite_descubierto = limite_descubierto

    def retirar(self, cantidad):                                        #modifico método que ya existía.
        if cantidad> self.saldo + self.limite_descubierto:
            print("Excede el límite descubierto.")
        elif cantidad <=0:
            print("Cantidad inválida para retirar.")
        else:
            self.saldo -= cantidad
            print(f"Retiró: U$D {cantidad}. Saldo Actual: U$D {self.saldo}")


#Polimorfismo(objetos comportandose de manera similar, en este caso el método retirar es distinto para cada tipo de cuenta)

def procesar_retiro(cuenta, cantidad):      #recibe cualquier objeto que sea una "CuentaBancaria"
    cuenta.retirar(cantidad)

if __name__ == '__main__':
    cuenta_ahorro = CuentaAhorro ("María Pía", 2500)
    cuenta_corriente = CuentaCorriente("Ezequiel Coria", 5000)

    print("\n   Operaciones en Cuenta de Ahorro --")
    cuenta_ahorro.depositar(200)
    cuenta_ahorro.aplicar_interes()
    procesar_retiro(cuenta_ahorro, 300)

    print("\n Operaciones en Cuenta Corriente --")
    cuenta_corriente.depositar(100)
    procesar_retiro(cuenta_corriente, 800)
