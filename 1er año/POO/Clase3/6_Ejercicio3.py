"""
3. Modela una clase Persona con atributos nombre y edad. Incluye un método presentarse. 
Crea una subclase Alumno que herede de Persona y añada un atributo carrera y un método estudiar (debe imprimir que el alumno
está estudiando su carrera). 
Implementa un método adicional cambiar_carrera que permita al alumno cambiar su carrera, asegurándose de que la nueva carrera no sea igual a la anterior.
"""

class Persona:
    def __init__(self, nombre, edad):
        self.nombre= nombre
        self.edad= edad

    def Presentarse(self):
        print("Hola, como estan?. Mi nombre es "+ self.nombre+ " tengo "+self.edad +  " años.")

class Alumno(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera= carrera
    
    def Estudiar(self):
        print("Hola, estoy estudiando "+ self.carrera)

    def cambiar_carrera(self):
        nueva_carrera="N/A"
        while self.carrera != nueva_carrera:
            nueva_carrera= input("Ingrese la carrera que desea cambiar.")
            if nueva_carrera == self.carrera:
                print("Ingrese una carrera distinta a la que desea cambiar.")
                nueva_carrera="N/A"
            else:
                self.carrera= nueva_carrera
            print("Usted se cambio a la carrera de "+ self.carrera)

al1=Alumno("Daniel", "28","Analisis de Sistemas")
al1.Presentarse()
al1.Estudiar()
al1.cambiar_carrera()