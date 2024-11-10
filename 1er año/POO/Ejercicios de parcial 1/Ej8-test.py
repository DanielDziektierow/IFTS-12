"""Crea una clase Reserva con los siguientes atributos:

nro_reserva (int): Nro del reserva
nombre_huesped (string): Nombre del huésped.
numero_habitacion (int): Número de habitación reservada.
fecha_entrada (string): Fecha de entrada.
fecha_salida (string): Fecha de salida.
"""
class Reserva:
    def __init__(self, nro_reserva, nombre_huesped, numero_habitacion, fecha_entrada, fecha_salida):
        self.nro_reserva= nro_reserva
        self.nombre_huesped= nombre_huesped
        self.numero_habitacion=numero_habitacion
        self.fecha_entrada=fecha_entrada
        self.fecha_salida=fecha_salida

    def infoReserva(self):
        return f"\nN Reserva: {self.nro_reserva}\nNombre de huesped: {self.nombre_huesped}\nN Habitacion: {self.numero_habitacion}\nEntrada: {self.fecha_entrada}\nSalida: {self.fecha_salida}\n"
        
"""
Implementa una clase GestorReservas que gestione una lista de reservas. Esta clase tendrá los siguientes métodos:

agregar_reserva(reserva): Agrega una reserva a la lista.
eliminar_reserva(nro_reserva): Elimina una reserva por el nro de reserva.
mostrar_reservas(): Muestra todas las reservas con su nro, nombre, número de habitación y fechas de entrada y salida.
Implementa las clases necesarias en Python en el archivo gestion_reservas.py.
"""
class GestorReservas:
    def __init__(self):
        self.reservas=[]

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def eliminar_reserva(self, nReserva):
        for reserva in self.reservas:
            if reserva.nro_reserva == nReserva:
                self.reservas.remove(nReserva)
                print(f"Reserva '{nReserva}' eliminada.")
                

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(reserva.infoReserva())
"""
Dibuja un diagrama de clases en UML mostrando la relación entre Reserva y GestorReservas. Exporta el diagrama como gestion_reservas.png.

Al ejecutar el archivo gestion_reservas.py, debe mostrar por pantalla:

Solicitar un nro de reserva.
Mostrar la reserva con su nombre, número de habitación, fecha de entrada y fecha de salida.

"""

#Test
r1=Reserva(12, "Daniel", 12, "15-02-2024", "18-02-2024")
gr1=GestorReservas()
gr1.agregar_reserva(r1)
gr1.mostrar_reservas()