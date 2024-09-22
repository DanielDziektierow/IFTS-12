"""4. Sistema de Gestión de Tareas 
Desarrolla un sistema de gestión de tareas para un equipo de trabajo. 
La capa de presentación permitirá añadir, modificar o eliminar tareas. 
La capa de negocio controlará la prioridad y las fechas límite. 
La capa de datos guardará la información de las tareas.
"""
MAX_PRIORIDAD=5
import datetime
    
# Capa de Datos
class BaseDeDatos:
    def __init__(self):
        self.nTarea = {"001":{
                                    "Nombre":"Epic Cliente",
                                    "Prioridad": 5,
                                    "Vencimiento": datetime.datetime(2024,11,5)},
                        "002":{
                                    "Nombre":"Feature1",
                                    "Prioridad": 2,
                                    "Vencimiento": datetime.datetime(2024,10,5)},
                        "003":{
                                    "Nombre":"PBI1",
                                    "Prioridad": 1,
                                    "Vencimiento": datetime.datetime(2024,11,5)},
                                    }
    def buscarTarea(self, idTarea):
        return self.nTarea.get(idTarea)
    
    def mostrarNombre(self,idTarea):
        return self.nTarea.get(idTarea).get("Nombre")
    
    def mostrarPrioridad(self, idTarea):
        return self.nTarea.get(idTarea).get("Prioridad")
    
    def mostrarVencimiento(self, idTarea):
        return self.nTarea.get(idTarea).get("Vencimiento")
    
    def eliminarTarea(self, idTarea):
        self.nTarea.pop(idTarea)
    
    def actualizarPrioridad(self, idTarea, Prioridad):
        self.nTarea.get(idTarea).update({"Prioridad": Prioridad})
        

# Capa de Negocio
class LogicaDeNegocio:
    def __init__(self, baseDatos):
        self.baseDatos = baseDatos
 
    def verificarDisponibilidad(self, idTarea):
        Tarea = self.baseDatos.buscarTarea(idTarea)
        if Tarea:
            return f"Tarea disponible: {self.baseDatos.mostrarNombre(idTarea)}, Prioridad: {self.baseDatos.mostrarPrioridad(idTarea)}, Vencimiento: {self.baseDatos.mostrarVencimiento(idTarea)}"
        else:
            return "Tarea no encontrada"

    def controlarVencimiento(self, idTarea):
        vencimiento= self.baseDatos.mostrarVencimiento(idTarea)
        if vencimiento < datetime.datetime.today():
            self.baseDatos.eliminarTarea(idTarea)
    
    def controlarPrioridad(self, idTarea):
        prioridad= self.baseDatos.mostrarPrioridad(idTarea)
        if prioridad >= MAX_PRIORIDAD:
            print("Maxima prioridad.")

    

# Capa de Presentación
class Interfaz:
    def __init__(self, logicaNegocio):
        self.logicaNegocio = logicaNegocio
    
    def verificarInventario(self,idTarea):
        resultado=self.logicaNegocio.verificarDisponibilidad(idTarea)
        print(resultado)

    def agregarTarea(self, tarea):                          #tarea debe ser tipo dict
        self.logicaNegocio.baseDatos.nTarea.update(tarea)
    
    def eliminarTarea(self, idTarea):
        self.logicaNegocio.baseDatos.eliminarTarea(idTarea)

    def modificarTarea(self, idTarea, modificacion):        #modificacion debe ser tipo dict
        self.logicaNegocio.baseDatos.nTarea[idTarea].update(modificacion)
#------------------------------------------------------------------------

# Instanciar las clases y realizar la búsqueda
baseDatos = BaseDeDatos()
logicaNegocio = LogicaDeNegocio(baseDatos)
interfaz = Interfaz(logicaNegocio)

# Simulación de búsqueda de libro
interfaz.verificarInventario("001") # Salida: Tarea disponible: Epic Cliente, Prioridad: 5, Vencimiento: 2024-11-05 00:00:00
interfaz.verificarInventario("002")
interfaz.verificarInventario("003")
interfaz.verificarInventario("005") # Salida: Tarea no encontrado
print("\n---------------------------\n")
interfaz.agregarTarea({"005" : {
                                    "Nombre":"Relevamiento",
                                    "Prioridad": 5,
                                    "Vencimiento": datetime.datetime(2024,11,5)}})

interfaz.verificarInventario("005") # Salida: Tarea no encontrado
print("\n---------------------------\n")
interfaz.modificarTarea("003", {"Prioridad": 3})
interfaz.verificarInventario("003")
print("\n---------------------------\n")
interfaz.eliminarTarea("002")
interfaz.verificarInventario("002")