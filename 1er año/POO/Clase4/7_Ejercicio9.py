"""3. Combinación de Modularidad y Sobrecarga: Diseña un módulo OperacionesMatematicas que incluya una clase
Calculadora. 
Añade métodos sobrecargados para realizar diferentes operaciones matemáticas básicas como suma
y resta."""

class Calculadora:
    def __init__(self,op1, op2, op3=None):
        self.op1= op1
        self.op2= op2
        if op3 is None:
            self.op3=0
        else:
            self.op3=op3
    
    def suma(self):
        return self.op1 + self.op2 + self.op3
    
    def resta(self):
        return self.op1 - self.op2 - self.op3