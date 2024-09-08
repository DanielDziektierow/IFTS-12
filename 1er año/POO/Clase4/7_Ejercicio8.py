"""2. Sobrecarga de Métodos: Crea una clase Rectangulo
que pueda calcular el área de un rectángulo usando diferentes firmas de métodos: 
uno que reciba el largo y el ancho, y otro que reciba solo el largo (para un cuadrado).
"""
class Rectangulo:
    def __init__(self,largo, ancho=None):
        self.largo= largo
        if ancho is not None:
            self.ancho= ancho
        else:
            self.ancho= largo
    
    def calcular_area(self):
        return self.largo * self.ancho

rect= Rectangulo(5,2)
print(rect.calcular_area())