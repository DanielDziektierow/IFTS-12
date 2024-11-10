# Crea una clase Cuenta con métodos para depositar y retirar dinero.
# Maneja excepciones para evitar retirar más dinero del que tiene la cuenta.
# e ingresar saldos menores a 10
class Cuenta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, cantidad):
        if cantidad > 10 :
            self.saldo += cantidad
        else :
            # Excepción para evitar ingresar dinero menor a 10
            raise ValueError("Sólo se permiten montos mayor a 10")

    def retirar(self, cantidad):

        if cantidad <= self.saldo :
            self.saldo -= cantidad
        else :
            # Excepción para evitar retirar más dinero del que tiene la cuenta
            raise ValueError("Saldo insuficiente")

    def mostrar_saldo(self):
        print(self.saldo)

mi_cuenta = Cuenta()

try :
    mi_cuenta.depositar(100)
except ValueError as e:
    print(e)

try :
    mi_cuenta.retirar(90)
except ValueError as e:
    print(e)

mi_cuenta.mostrar_saldo() 
