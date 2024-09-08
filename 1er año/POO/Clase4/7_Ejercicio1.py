"""1. Asociación Básica: Modela una relación entre un Doctor y Paciente, donde un Doctor tiene múltiples Pacientes.
Implementa una clase Doctor y Paciente, y muestra cómo se relacionan.
"""
class Paciente:
    def __init__(self, apellido):
        self.apellido= apellido

    def MostrarPaciente(self):
        print(self.apellido)

class Doctor:
    def __init__(self, nombre):
        self.nombre= nombre
        self.pacientes= []

    def AgregarPaciente(self, paciente):
        self.pacientes.append(paciente)

    def MostrarPacientes(self):
        for i in self.pacientes:
            i.MostrarPaciente()

pacin1= Paciente('Steiner')
pacin2= Paciente('Gomez')

dr1= Doctor('Enrique Hernandez')

dr1.AgregarPaciente(pacin1)
dr1.AgregarPaciente(pacin2)

#pacin1.MostrarPaciente()

dr1.MostrarPacientes()
