"""Ejercicio 1
Crea un sistema para gestionar empleados con tres capas. 
La capa de datos almacena los datos de los empleados, 
la capa de negocio valida que el sueldo sea positivo, 
y la capa de presentación permite agregar y mostrar empleados.

Salida esperada

Si se ingresan datos válidos (por ejemplo, nombre: Ana y sueldo: 3500):
Nombre del empleado: Ana
Sueldo: 3500
Empleado agregado.

Si se ingresa un sueldo negativo:
Nombre del empleado: Ana
Sueldo: -1000
Traceback (most recent call last):
...
ValueError: El sueldo debe ser positivo."""
# Capa de datos
class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

# Capa de negocio
class GestionEmpleados:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, nombre, sueldo):
        if sueldo <= 0:
            raise ValueError("El sueldo debe ser positivo.")
        nuevo_empleado = Empleado(nombre, sueldo)
        self.empleados.append(nuevo_empleado)

    def obtener_empleados(self):
        return self.empleados

# Capa de presentación
class InterfazEmpleados:
    def __init__(self):
        self.gestion = GestionEmpleados()

    def agregar_empleado(self, nombre, sueldo):
        try:
            self.gestion.agregar_empleado(nombre, sueldo)
            print(f"Empleado agregado: {nombre}, Sueldo: {sueldo}")
        except ValueError as e:
            print(f"\n-->Error: {e}")

    def mostrar_empleados(self):
        empleados = self.gestion.obtener_empleados()
        if empleados:
            print("\nLista de empleados:")
            for empleado in empleados:
                print(f"Nombre: {empleado.nombre}, Sueldo: {empleado.sueldo}")
        else:
            print("No hay empleados registrados.")

# Ejemplo de uso
interfaz = InterfazEmpleados()

# Agregar empleados
interfaz.agregar_empleado("Ana", 3500)   # Sueldo positivo
interfaz.agregar_empleado("Luis", 4500)  # Sueldo positivo
interfaz.agregar_empleado("Pedro", -500)  # Sueldo negativo, debería lanzar un error

# Mostrar empleados
interfaz.mostrar_empleados()
