"""5. Sobrecarga en Diferentes Contextos: Implementa una clase Conversor 
que tenga métodos sobrecargados para convertir temperaturas (Celsius a Fahrenheit), 
y distancias (Kilómetros a Millas). 
Simula la sobrecarga en Python."""

class Conversor:
    def __init__(self,tod = None):
        if tod is None:
            self.tod=0
        else:
            self.tod=tod

    def convertir_fahrenheit(self, temp=None):
        if temp is None:
            return self.tod * 9 / 5 + 32
        else:
            return temp * 9 / 5 + 32
        
    def convertir_millas(self, dist= None):
        if dist is None:
            return self.tod / 1.609
        else:
            return dist / 1.609
    
temp= Conversor(5)
print(temp.convertir_fahrenheit())
print(temp.convertir_fahrenheit(10))

dist= Conversor(5000)
print(dist.convertir_millas())
print(dist.convertir_millas(1500))