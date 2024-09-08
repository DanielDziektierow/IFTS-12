"""1. Modularidad: Diseña un sistema de gestión de bibliotecas dividiéndolo en módulos como Catalogo, Prestamos, y
Usuarios. 
Implementa estos módulos en Python.
"""

class Catalogo:
    def __init__(self):
        self.titulo= []

    def agregar_libro(self,titulo):
        self.titulo.append(titulo)


class Prestamo(Catalogo):
    def __init__(self):
        super().__init__()
        self.usuarios= []
        self.titulo= []
    
    def mostrar_libros(self):
        for i in self.libros:
            print(i)

    def prestar(self,libro):
        self.titulo.remove(libro)

class Usuario:
    def __init__(self,nombre,apellido,dni):
        self.nombre= nombre
        self.apellido= apellido
        self.dni= dni
    
    def prestar_libro(prestamo, libro):
        pres= Prestamo(prestamo)
        pres.prestar(libro)

