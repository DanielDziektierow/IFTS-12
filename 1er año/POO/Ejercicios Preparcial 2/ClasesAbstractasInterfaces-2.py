"""2. Crea una interfaz IDispositivo con el método encender. 
Implementa dos clases, Televisor y Radio, que tengan comportamientos específicos al encenders."""
from abc import ABC, abstractmethod

class IDispositivo(ABC):
    @abstractmethod

    def encender(self):
        pass

class Televisor(IDispositivo):
    def encender(self):
        print("Television encendida.")

class Radio(IDispositivo):
    def encender(self):
        print("Radio encendida.")

# Ejemplo de uso
tv = Televisor()
radio = Radio()

tv.encender()     # Salida: Encendiendo el televisor. Disfrute de su programa.
radio.encender()  # Salida: Encendiendo la radio. Escuche su emisora favorita.