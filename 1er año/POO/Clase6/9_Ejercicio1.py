"""1. Sistema de Reservas de Vuelos Modela un sistema de reservas de vuelos con un modelo de tres capas. 
La capa de presentación permitirá a los usuarios seleccionar un vuelo. 
La capa de negocio verificará la disponibilidad 
y la capa de datos consultará la base de datos de vuelos."""

# Capa de Datos
class BaseDeDatos:
    def __init__(self):
        self.nVuelo = {
        "001": "UHA",
        "002": "BRC",
        "003": "IGZ"
        } 

    def buscarVuelo(self, idVuelo):
        return self.nVuelo.get(idVuelo, None)

# Capa de Negocio
class LogicaDeNegocio:
    def __init__(self, baseDatos):
        self.baseDatos = baseDatos
 
    def verificarDisponibilidad(self, idVuelo):
        vuelo = self.baseDatos.buscarVuelo(idVuelo)
        if vuelo:
            return f"Vuelo disponible: {vuelo}"
        else:
            return "Vuelo no encontrado"

# Capa de Presentación
class Interfaz:
    def __init__(self, logicaNegocio):
        self.logicaNegocio = logicaNegocio
    
    def buscarVuelo(self,idVuelo):
        resultado=self.logicaNegocio.verificarDisponibilidad(idVuelo)
        print(resultado)

#------------------------------------------------------------------------

# Instanciar las clases y realizar la búsqueda
baseDatos = BaseDeDatos()
logicaNegocio = LogicaDeNegocio(baseDatos)
interfaz = Interfaz(logicaNegocio)

# Simulación de búsqueda de libro
interfaz.buscarVuelo("001") # Salida: Libro disponible: El Principito
interfaz.buscarVuelo("005") # Salida: Libro no encontrado