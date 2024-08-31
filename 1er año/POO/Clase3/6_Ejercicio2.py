"""
2. Crea una clase CuentaBancaria con los atributos titular y saldo. 
Incluye métodos depositar y retirar. 
Crea una subclase CuentaAhorro que agregue un atributo interes y un método para aplicar el interés al saldo.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.saldo= saldo
    
    def Depositar(self):
        print("Depositando...")
    
    def Retirar(self):
        print("Retirando...")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes= interes
     
    def AplicarInteres(self):
        print("Aplicando interes de "+ self.interes+ "...")


cb= CuentaAhorro("Daniel","$4", "10")
cb.Depositar()
cb.Retirar()
cb.AplicarInteres()