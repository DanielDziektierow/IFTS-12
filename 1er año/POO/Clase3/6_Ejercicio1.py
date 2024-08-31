"""1. Crea una clase Animal con atributos nombre y especie. 
Incluye un método hacer_sonido que imprima un sonido genérico.
Crea una subclase Perro que herede de Animal y sobreescriba el método hacer_sonido para imprimir"Guau".
"""

class Animal:
    def __init__(self, nombre, especie):
        self.nombre= nombre
        self.especie= especie

    def hacer_sonido(self):
        print("Grrr.")

class Perro(Animal):
    def __init__(self, nombre, especie):
        self.nombre= nombre
        self.especie= especie

    def hacer_sonido(self):
        print("Guau")

pp= Perro("ppito","Perro")
pp.hacer_sonido()