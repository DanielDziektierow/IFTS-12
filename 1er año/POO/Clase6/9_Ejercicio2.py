"""2. Sistema de Gestión de Inventario
Diseña un sistema que gestione inventario en un almacén. La capa de presentación permitirá al usuario verificar
el inventario.
La capa de negocio gestionará la lógica de reposición automática.
La capa de datos almacenará la cantidad de productos.
"""

# Capa de Datos
class BaseDeDatos:
    def __init__(self):
        self.nProducto = {"001":{"Nombre":"Galletitas",
                                "Cantidad": 5},
                        "002":{"Nombre":"Leche",
                                "Cantidad": 3},
                        "003":{"Nombre":"polenta",
                                "Cantidad": 15}}
    def buscarProducto(self, idProducto):
        return self.nProducto.get(idProducto)
    
    def mostrarNombre(self,idProducto):
        return self.nProducto.get(idProducto).get("Nombre")
    
    def mostrarCantidad(self, idProducto):
        return self.nProducto.get(idProducto).get("Cantidad")
    
    def actualizarCantidad(self, idProducto, cantidad):
        self.nProducto.get(idProducto).update({"Cantidad": cantidad})
        

# Capa de Negocio
class LogicaDeNegocio:
    def __init__(self, baseDatos):
        self.baseDatos = baseDatos
 
    def verificarDisponibilidad(self, idProducto):
        producto = self.baseDatos.buscarProducto(idProducto)
        if producto:
            return f"Producto disponible: {self.baseDatos.mostrarNombre(idProducto)}, Cantidad: {self.baseDatos.mostrarCantidad(idProducto)}"
        else:
            return "Producto no encontrado"

    def retirarProducto(self, idProducto):
        cantPrevia= self.baseDatos.mostrarCantidad(idProducto)
        self.baseDatos.actualizarCantidad(idProducto, cantPrevia-1)


# Capa de Presentación
class Interfaz:
    def __init__(self, logicaNegocio):
        self.logicaNegocio = logicaNegocio
    
    def verificarInventario(self,idProducto):
        resultado=self.logicaNegocio.verificarDisponibilidad(idProducto)
        print(resultado)
    def disminuirProducto(self, idProducto):
        self.logicaNegocio.retirarProducto(idProducto)

#------------------------------------------------------------------------

# Instanciar las clases y realizar la búsqueda
baseDatos = BaseDeDatos()
logicaNegocio = LogicaDeNegocio(baseDatos)
interfaz = Interfaz(logicaNegocio)

# Simulación de búsqueda de libro
interfaz.verificarInventario("001") # Salida: Producto disponible: Galletitas, Cantidad: 5
interfaz.disminuirProducto("001")
interfaz.verificarInventario("001")
#interfaz.verificarInventario("005") # Salida: Libro no encontrado