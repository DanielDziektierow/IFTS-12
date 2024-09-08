"""5. Encapsulamiento Avanzado: Diseña una clase Biblioteca que tenga una lista de Libros.
Los libros deben ser accesibles solo mediante métodos de la Biblioteca, como 
agregar_libro, remover_libro, y mostrar_libros."""
class Biblioteca:
    def __init__(self):
        self.__libro= []

    def agregar_libro(self, titulo):
        self.__libro.append(titulo)
    
    def mostrar_libros(self):
        for i in self.__libro:
            print(i)
    
    def remover_libro(self, titulo):
        self.__libro.remove(titulo)

b1= Biblioteca()
b1.agregar_libro("HP")
b1.agregar_libro("El principito")
b1.agregar_libro("El fantasma de canterville")
b1.mostrar_libros()
b1.remover_libro("HP")
b1.mostrar_libros()