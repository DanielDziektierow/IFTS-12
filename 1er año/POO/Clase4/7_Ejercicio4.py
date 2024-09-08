"""4. Encapsulamiento Simple: Crea una clase CuentaBancaria con atributos saldo (privado) y métodos para depositar,
retirar, y mostrar_saldo. 
Implementa un control de acceso para evitar que el saldo sea negativo.
"""
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo= saldo
    
    def depositar(self, deposito):
        if deposito >0:
            self.__saldo= deposito + self.__saldo
        else:
            self.__saldo= 0

    def retirar(self, retiro):
        if self.__saldo - retiro>0:
            self.__saldo= self.__saldo - retiro
        else:
            self.__saldo=self.__saldo

    def mostrar_saldo(self):
        print(self.__saldo)

cb1= CuentaBancaria(40)
cb1.depositar(800)
cb1.retirar(100)
cb1.mostrar_saldo()