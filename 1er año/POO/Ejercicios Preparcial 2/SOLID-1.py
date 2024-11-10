""" 1. Crea una clase Pedido que tenga la responsabilidad de almacenar los detalles de un pedido 
y una clase CalcularTotal que calcule el total del pedido aplicando impuestos.

Salida esperada

Total con impuestos: 402.5
"""
class Pedido:
    def __init__(self, subtotal):
        self.subtotal = subtotal

class CalcularTotal:
    def __init__(self, pedido, tasa_impuesto):
        self.pedido = pedido
        self.tasa_impuesto = tasa_impuesto

    def calcular(self):
        total = self.pedido.subtotal * (1 + self.tasa_impuesto)
        return total

# Crear una instancia de Pedido con el subtotal
pedido = Pedido(subtotal=350.0)

# Crear una instancia de CalcularTotal con la tasa de impuesto
calculo_total = CalcularTotal(pedido=pedido, tasa_impuesto=0.15)

# Imprimir el resultado
print("Total con impuestos:", calculo_total.calcular())
