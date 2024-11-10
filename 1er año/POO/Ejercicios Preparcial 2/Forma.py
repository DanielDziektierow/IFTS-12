# Define una interfaz Forma con métodos area() y perimetro().
# Implementa las clases Triangulo y Rectangulo, asegurándote
# de que ambas clases implementen los métodos de la interfaz.
from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Triangulo(Forma):
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2

class Rectangulo(Forma):
    def __init__(self, lado1, lado2):
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return self.lado1 * self.lado2

    def perimetro(self):
        return (self.lado1 + self.lado2) * 2    