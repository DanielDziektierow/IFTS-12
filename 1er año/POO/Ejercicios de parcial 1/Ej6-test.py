"""Crea una clase Proyecto con los siguientes atributos:

nombre (string): Nombre del proyecto.
descripcion (string): Descripción del proyecto.
fecha_inicio (string): Fecha de inicio del proyecto."""
class Proyecto:
    def __init__(self,nombre, descripcion, fecha_inicio):
        self.nombre=nombre
        self.descripcion=descripcion
        self.fecha_inicio=fecha_inicio
    
    def mostrar_proyecto(self):
        return f"\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nFecha de inicio: {self.fecha_inicio}\n"

"""Implementa una clase GestorProyectos que gestione una lista de proyectos. Esta clase tendrá los siguientes métodos:
agregar_proyecto(proyecto): Agrega un proyecto a la lista.
eliminar_proyecto(nombre): Elimina un proyecto por su nombre.
mostrar_proyectos(): Muestra todos los proyectos con su nombre, descripción y fecha de inicio.
Implementa las clases necesarias en Python en el archivo gestion_proyectos.py.
"""
class GestorProyectos:
    def __init__(self):
        self.proyectos=[]

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def mostrar_proyectos(self):
        for proy in self.proyectos:
            print(proy.mostrar_proyecto())

    def eliminar_proyecto(self, nombre):
        for proy in self.proyectos:
            if proy.nombre == nombre:
                self.proyectos.remove(proy)
                print(f"Proyecto '{nombre}' eliminado.")
"""
Dibuja un diagrama de clases en UML mostrando la relación entre Proyecto y GestorProyectos. Exporta el diagrama como gestion_proyectos.png.

Al ejecutar el archivo gestion_proyectos.py, debe mostrar por pantalla:

Solicitar el nombre del proyecto y eliminar el proyecto mostrando sus datos: nombre, descripción y fecha de inicio.
Todos sus métodos debe funcionar correctamente
"""
gp1=GestorProyectos()
op=777
while op!=-1:
    op=int(input("Ingrese 1 para agregar proyecto.\nIngrese 2 para mostrar los proyectos.\nIngrese 3 para eliminar algun proyecto.\nIngrese -1 para terminar."))
    if op==1:
        nombre=input("\nIngrese el nombre del proyecto.")
        descripcion=input("Ingrese la descripcion del proyecto.")
        fechaInicio=input("Ingrese fecha de inicio del proyecto.")
        p1= Proyecto(nombre, descripcion, fechaInicio)
        gp1.agregar_proyecto(p1)
    elif op==2:
        gp1.mostrar_proyectos()
    elif op==3:
        nombre=input("Ingrese el nombre del proyecto a eliminar.")
        gp1.eliminar_proyecto(nombre)
    else:
        op=-1
