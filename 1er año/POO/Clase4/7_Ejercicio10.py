"""4. Modularidad Avanzada: Imagina un sistema de gestión de reservas de un hotel. 
Divide el sistema en módulos como Reservas, Clientes, y Habitaciones. 
Implementa estos módulos en Python y define cómo se comunican entre sí.
"""
class Reserva:
    def __init__(self):
        self.cliente= []

    def agregar_cliente(self,cliente):
        self.cliente.append(cliente)
    
    def mostrar_reserva(self):
        for i in self.cliente:
            print(i)

class Habitacion:
    def __init__(self):
        self.cliente= []
    
    def agregar_cliente(self,cliente):
        self.cliente.append(cliente)
    
    def mostrar_habitacion(self):
        for i in self.cliente:
            print(i)

