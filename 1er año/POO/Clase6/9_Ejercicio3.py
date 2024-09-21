"""Sistema de Facturación
Crea un sistema de facturación usando el modelo de tres capas.
La capa de presentación generará la factura. 
La capa de negocio calculará los impuestos y descuentos. 
La capa de datos guardará la información de facturación.
"""

# Capa de Datos
class BaseDeDatos:
    def __init__(self):
        self.nFactura = {
        "001": 5000,
        "002": 6000,
        "003": 7000
        } 

    def buscarFactura(self, idFactura):
        return self.nFactura.get(idFactura)

# Capa de Negocio
class LogicaDeNegocio:
    def __init__(self, baseDatos):
        self.baseDatos = baseDatos
 
    def verificarDisponibilidad(self, idFactura):
        Factura = self.baseDatos.buscarFactura(idFactura)
        if Factura:
            return f"Factura disponible: {Factura}"
        else:
            return "Factura no encontrado"
    
    def calcularImpuesto(self, idFactura):
        valorFactura = self.baseDatos.buscarFactura(idFactura)
        return  valorFactura * 1.21

    def calcularDescuento(self, idFactura):
        valorFactura = self.baseDatos.buscarFactura(idFactura)
        return valorFactura * 0.15


# Capa de Presentación
class Interfaz:
    def __init__(self, logicaNegocio):
        self.logicaNegocio = logicaNegocio
    
    def buscarFactura(self,idFactura):
        resultado=self.logicaNegocio.verificarDisponibilidad(idFactura)
        print(resultado)
        print(f"Hay un dto. de {self.logicaNegocio.calcularDescuento(idFactura)}")
        print(f"El IVA es de {self.logicaNegocio.calcularImpuesto(idFactura)}")

#------------------------------------------------------------------------

# Instanciar las clases y realizar la búsqueda
baseDatos = BaseDeDatos()
logicaNegocio = LogicaDeNegocio(baseDatos)
interfaz = Interfaz(logicaNegocio)

# Simulación de búsqueda de libro
interfaz.buscarFactura("003") # Salida: Libro disponible: El Principito
#interfaz.buscarFactura("005") # Salida: Libro no encontrado