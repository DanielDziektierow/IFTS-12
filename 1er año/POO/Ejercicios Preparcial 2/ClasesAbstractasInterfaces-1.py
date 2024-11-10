"""1. Define una clase abstracta Instrumento con el método tocar. Crea clases concretas
Guitarra y Piano que implementen el método tocar con mensajes distintos.
"""
from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod

    def tocar(self):
        pass

class Guitarra(Instrumento):

    def tocar(self):
        return "Tocando la guitarra."
    
class Piano(Instrumento):

    def tocar(self):
        return "Tocando el piano."

p1= Piano()
g1= Guitarra()

print(p1.tocar())
print("\n")
print(g1.tocar())