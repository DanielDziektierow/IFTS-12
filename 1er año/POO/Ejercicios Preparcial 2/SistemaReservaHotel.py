#Sistema de Reservas de Hotel
"""Crea un sistema para gestionar reservas en un hotel. 
Debe cumplir con lo siguiente:
    1. Implementa una clase abstracta Habitacion con un método abstracto
    mostrar_detalles."""
from abc import ABC, abstractmethod
from datetime import datetime

class Habitacion(ABC):
    @abstractmethod

    def mostrar_detalles(self):
        pass

"""
    2. Define una clase HabitacionEstandar y una clase HabitacionSuite que
    heredan de Habitacion e implementan mostrar_detalles para describir los tipos
    de habitaciones.
"""
class HabitacionEstandar(Habitacion):
    def mostrar_detalles(self):
        return "Habitación: Estándar"

class HabitacionSuite(Habitacion):
    def mostrar_detalles(self):
        return "Habitación: Suite"
"""
    3. Implementa la clase Reserva que almacena detalles de una reserva y la clase
    GestorReservas para gestionar la lista de reservas, aplicando el principio de
    Responsabilidad Única.
"""
# Capa de negocio
class Reserva:
    def __init__(self, cliente, habitacion, fecha_entrada, fecha_salida):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida
        self.validar_fechas()

    def validar_fechas(self):
        if self.fecha_salida < self.fecha_entrada:
            raise FechaInvalidaError("Error: La fecha de salida no puede ser anterior a la fecha de entrada.")

    def mostrar_reserva(self):
        detalles_habitacion = self.habitacion.mostrar_detalles()
        return (
            f"Reserva agregada.\n"
            f"Detalles de la reserva:\n"
            f"Cliente: {self.cliente}\n"
            f"{detalles_habitacion}\n"
            f"Fecha de entrada: {self.fecha_entrada}\n"
            f"Fecha de salida: {self.fecha_salida}"
        )

# Capa de negocio
class GestorReservas:
    def __init__(self):
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def obtener_reservas(self):
        return self.reservas
"""
    4. Crea un módulo InterfazReservas en la capa de presentación que permita
    agregar y mostrar reservas.
"""
# Capa de presentación - Interfaz de reservas

class InterfazReservas:
    def __init__(self):
        self.gestor = GestorReservas()

    def agregar_reserva(self, cliente, tipo_habitacion, fecha_entrada, fecha_salida):
        # Crear la habitación según el tipo
        if tipo_habitacion.lower() == "estandar":
            habitacion = HabitacionEstandar()
        elif tipo_habitacion.lower() == "suite":
            habitacion = HabitacionSuite()
        else:
            print("Error: Tipo de habitación inválido.")
            return

        # Convertir fechas de string a objetos datetime
        try:
            fecha_entrada = datetime.strptime(fecha_entrada, "%Y-%m-%d")
            fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d")
            reserva = Reserva(cliente, habitacion, fecha_entrada, fecha_salida)
            self.gestor.agregar_reserva(reserva)
            print(reserva.mostrar_reserva())
        except FechaInvalidaError as e:
            print(e)
        except ValueError:
            print("Error: Formato de fecha incorrecto. Use AAAA-MM-DD.")

    def mostrar_reservas(self):
        reservas = self.gestor.obtener_reservas()
        if reservas:
            for reserva in reservas:
                print(reserva.mostrar_reserva())
        else:
            print("No hay reservas registradas.")

"""
    5. Agrega una excepción FechaInvalidaError que se lance si la fecha de salida es
    anterior a la fecha de entrada.
"""
# Excepción personalizada para fechas inválidas
class FechaInvalidaError(Exception):
    pass
"""
Salida esperada
    Si se ingresa una fecha de salida anterior a la fecha de entrada:
    Error: La fecha de salida no puede ser anterior a la fecha de entrada.

    Si la reserva es exitosa:
    Reserva agregada.

Detalles de la reserva:
    Cliente: Juan Pérez
    Habitación: Estandar
    Fecha de entrada: 2024-11-05
    Fecha de salida: 2024-11-10"""
# Ejemplo de uso
interfaz = InterfazReservas()
# Agregar una reserva correcta
interfaz.agregar_reserva("Juan Pérez", "estandar", "2024-11-05", "2024-11-10")
# Intento de agregar una reserva con error de fecha
print("\n")
interfaz.agregar_reserva("Ana López", "suite", "2024-11-15", "2024-11-10")
print("\n")
# Mostrar todas las reservas
interfaz.mostrar_reservas()