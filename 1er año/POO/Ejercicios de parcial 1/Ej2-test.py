"""Crea una clase Tarea con los siguientes atributos:

titulo (string): Título de la tarea.
descripcion (string): Descripción de la tarea.
estado (string): Estado de la tarea (e.g., "Pendiente", "En Progreso", "Completada").
"""
class Tarea:
    def __init__(self, titulo, descripcion, estado):
        self.titulo= titulo
        self.descripcion= descripcion
        self.estado= estado
    
    def __str__(self):
        return f"\nTítulo: {self.titulo}\nDescripción: {self.descripcion}\nEstado: {self.estado}"
"""
Implementa una clase GestorTareas que gestione una lista de tareas. Esta clase tendrá los siguientes métodos:

agregar_tarea(tarea): Agrega una tarea a la lista.
eliminar_tarea(titulo): Elimina una tarea por su título.
mostrar_tareas(): Muestra todas las tareas con su título, descripción y estado.
"""
class GestorTareas:
    def __init__(self):
        self.lisTarea= []
    
    def agregar_tarea(self, tarea):
        self.lisTarea.append(tarea)

    def mostrar_tareas(self):
        for i in self.lisTarea:
            print(i)
    

    def eliminar_tarea(self, titulo):
        for tarea in self.lisTarea:
            if tarea.titulo == titulo:
                self.lisTarea.remove(tarea)
                print(f"Tarea '{titulo}' eliminada.")
        
"""
Implementa las clases necesarias en Python en el archivo gestion_tareas.py.

Dibuja un diagrama de clases en UML mostrando la relación entre Tarea y GestorTareas. Exporta el diagrama como gestion_tareas.png.

Al ejecutar el archivo gestion_tareas.py, debe mostrar por pantalla:

Debe solicitar que cargue las tareas
Al finalizar debe mostrar la lista de tareas con su título, descripción y estado."""

  


#Test
gt1= GestorTareas()
op=777
while op!=-1:
    op=int(input("Ingrese 1 para agregar una tarea.\nIngrese 2 para mostrar las tareas.\nIngrese 3 para el estado de las tareas.\nIngrese -1 para terminar."))
    if op==1:
        titulo=input("\nIngrese el titulo de la tarea.")
        descripcion=input("Ingrese la descripcion de la tarea.")
        estado=input("Ingrese el estado de la tarea.")
        p1= Tarea(titulo, descripcion, estado)
        gt1.agregar_tarea(p1)
    elif op==2:
        gt1.mostrar_tareas()
    elif op==3:
        nombre=input("Ingrese el nombre de la tarea a eliminar.")
        gt1.eliminar_tarea(nombre)
    else:
        op=-1
