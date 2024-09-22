"""5. Sistema de Inscripción de Estudiantes 
Diseña un sistema donde los estudiantes puedan inscribirse en cursos. 
La capa de presentación permitirá ver y seleccionar cursos. 
La capa de negocio validará la inscripción 
y la capa de datos guardará la información del estudiante."""
CAPACIDAD_MAXIMA= 30

import datetime
    
# Capa de Datos
class BaseDeDatos:
    def __init__(self):
        self.nEstudiante = {"001":{
                                    "Nombre":"Daniel",
                                    "Materia": "Fisica",
                                    "Cantidad": 29},
                        "002":{
                                    "Nombre":"Alejandro",
                                    "Materia": "Biologia",
                                    "Cantidad": 30},
                        "003":{
                                    "Nombre":"Homero",
                                    "Materia": "Quimica",
                                    "Cantidad": 2},
                                    }
        self.nMaterias= {
            "001": {"Nombre":"Biologia",
                    "Cantidad":30},
            "002": {"Nombre":"Fisica",
                    "Cantidad":29},
            "003": {"Nombre":"Quimica",
                    "Cantidad":2}
        } 
    
    """def inscribirAlumno(self, idEstudiante, Prioridad):
        self.nEstudiante.get(idEstudiante).update({"Prioridad": Prioridad})"""
        

# Capa de Negocio
class LogicaDeNegocio:
    def __init__(self, baseDatos):
        self.baseDatos = baseDatos
 
    def validarInscripcion(self, id):
        cantAlumnos= self.baseDatos.nEstudiante.get(id).get("Cantidad")
        if cantAlumnos == CAPACIDAD_MAXIMA:
            print("Curso lleno.")
            return False
        else:
            print("Inscripcion validada.")
            return True

# Capa de Presentación
class Interfaz:
    def __init__(self, logicaNegocio):
        self.logicaNegocio = logicaNegocio
    
    def verificarInventario(self,idEstudiante):
        resultado=self.logicaNegocio.verificarDisponibilidad(idEstudiante)
        print(resultado)

    def agregarEstudiante(self, Estudiante):                          #Estudiante debe ser tipo dict
        if self.logicaNegocio.validarInscripcion("002"):
            self.logicaNegocio.baseDatos.nEstudiante.update(Estudiante)
        else:
            print("No hay vacante.")

    
    def eliminarEstudiante(self, idEstudiante):
        self.logicaNegocio.baseDatos.eliminarEstudiante(idEstudiante)

    def modificarEstudiante(self, idEstudiante, modificacion):        #modificacion debe ser tipo dict
        self.logicaNegocio.baseDatos.nEstudiante[idEstudiante].update(modificacion)

    def verCursos(self):
        print(self.logicaNegocio.baseDatos.nMaterias)
#------------------------------------------------------------------------

# Instanciar las clases y realizar la búsqueda
baseDatos = BaseDeDatos()
logicaNegocio = LogicaDeNegocio(baseDatos)
interfaz = Interfaz(logicaNegocio)

# Simulación de búsqueda de libro
interfaz.verCursos()

print("\n---------------------------\n")

interfaz.agregarEstudiante({"002" : {
                                    "Nombre":"Diego",
                                    "Materia": "Biologia",
                                    "Cantidad": 30}})
