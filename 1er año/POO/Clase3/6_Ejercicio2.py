"""
2. Crea una clase CuentaBancaria con los atributos titular y saldo. 
Incluye métodos depositar y retirar. 
Crea una subclase CuentaAhorro que agregue un atributo interes y un método para aplicar el interés al saldo.
"""

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular= titular
        self.saldo= saldo
    
    def Depositar(self, deposito):
        print(f"Depositando {deposito}...")
        self.saldo=self.saldo + int(deposito)
        print(f"Saldo de: {self.saldo}")
    
    def Retirar(self, extraccion):
        print(f"Retirando... {extraccion}")
        self.saldo=self.saldo - extraccion
        print(f"Saldo de: {self.saldo}")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, interes):
        super().__init__(titular, saldo)
        self.interes= interes
     
    def AplicarInteres(self):
        print(f"Aplicando interes de  {self.interes}...")
        self.saldo= self.saldo - self.interes


cb= CuentaAhorro("Daniel",400, 10)
cb.Depositar(800)
cb.Retirar(100)
cb.AplicarInteres()