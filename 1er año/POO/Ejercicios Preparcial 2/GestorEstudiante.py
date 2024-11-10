# Diseña un sistema de gestión de estudiantes que tenga una capa de datos,
# una capa de negocio y una capa de presentación. La capa de datos debe gestionar los
# estudiantes (agregar, eliminar), la capa de negocio debe validar que el nombre y
# la edad sean correctos, y la capa de presentación debe solicitar los datos del estudiante al usuario.

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad

# Capa de datos
class DatosEstudiante:
    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre :
                return self.estudiantes.remove(estudiante)

    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print('Nombre:', estudiante.nombre, 'Edad:', estudiante.edad)

# Capa de negocio
class GestorEstudiante:
    def __init__(self):
        self.db = DatosEstudiante()

    def agregar_estudiante(self, nombre, edad):
        if len(nombre) == 0:
            raise ValueError("Nombre inválido")
        if edad <= 0:
            raise ValueError("Edad inválida")

        self.db.agregar_estudiante(Estudiante(nombre,edad))

    def eliminar_estudiante(self, nombre):
        self.db.eliminar_estudiante(nombre)

    def mostrar_estudiantes(self):
        self.db.mostrar_estudiantes()

# Capa de presentación
class InterfazEstudiante:
    def __init__(self):
        self.gestor = GestorEstudiante()

    def menu(self):
        print('1. Agregar estudiante')
        print('2. Eliminar estudiante')
        print('3. Mostrar estudiantes')
        print('4. Salir')

    def ejecutar(self):
        self.menu()
        opcion = int(input('Elija una opción: '))
        while (opcion != 4) :
            if (opcion == 1) :
                nombre = input('Ingrese el nombre: ')
                edad = int(input('Ingresa la edad: '))
                self.gestor.agregar_estudiante(nombre, edad)

            if (opcion == 2) :
                nombre = input('Ingrese el nombre: ')

                self.gestor.eliminar_estudiante(nombre)

            if (opcion == 3) :
                self.gestor.mostrar_estudiantes()
                self.menu()
                
opcion = int(input('Elija una opción: '))

app = InterfazEstudiante()
app.ejecutar() 