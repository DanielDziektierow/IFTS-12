"""2. Agregación: Crea una clase Universidad que contenga múltiples Facultades, y una clase Facultad que tenga un
nombre y una lista de Carreras. Muestra cómo agregar facultades a una universidad y carreras a una facultad.
"""
class Facultad:
    def __init__(self, nombre):
        self.nombre= nombre
        self.carreras= []

    def AgregarCarreras(self, nombre):
        self.carreras.append(nombre)
    
    def MostrarCarrera(self):
        for i in self.carreras:
            print(i)

class Universidad:
    def __init__(self,nombre):
        self.nombre= nombre
        self.facultades= []
        
    def AgregarFacultades(self,facultad):
        self.facultades.append(facultad)

    def MostrarFacul(self):
        for i in self.facultades:
            print(i)


f1= Facultad("")
f1.AgregarCarreras("Ingenieria")
f1.AgregarCarreras("Licenciatura")
f1.MostrarCarrera()

u1= Universidad("UTN")
u1.AgregarFacultades("FRBA")
u1.AgregarFacultades("FRT")
u1.MostrarFacul()