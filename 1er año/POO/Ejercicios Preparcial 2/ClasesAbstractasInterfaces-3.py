"""3. Implementa una clase abstracta Animal con el método hacer_sonido. 
Crea las clases Perro y Gato que implementen el método para producir sonidos específicos."""

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau.")

class Gato(Animal):
    def hacer_sonido(self):
        print("Miau.")

perro= Perro()
gato= Gato()

perro.hacer_sonido()
gato.hacer_sonido()