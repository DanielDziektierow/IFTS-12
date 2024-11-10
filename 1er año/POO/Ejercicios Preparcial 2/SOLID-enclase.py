# (Responsabilidad Única): Diseña una clase Cliente que gestione
# solo la información del cliente y una clase ValidadorCliente que valide
# los datos del cliente (como el email o el número de teléfono). Implementa ambas clases.

"""
Principios SOLID:
S - Responsabilidad Única: Una clase debe tener una única razón para cambiar, es decir, debe cumplir solo un propósito.
O - Abierto/Cerrado: Las clases deben estar abiertas a extensión, pero cerradas a modificación.
L - Sustitución de Liskov: Los objetos de una clase derivada deben poder sustituir objetos de su clase base sin alterar el funcionamiento del programa.
I - Segregación de Interfaces: Las interfaces deben ser específicas, es decir, las clases no deberían tener que implementar métodos que no utilizan.
D - Inversión de Dependencias: Las clases deben depender de abstracciones, no de implementaciones concretas.
"""

class Cliente:
    def __init__(self, nombre, apellido, email, tel):
        self.nombre = nombre
        self.apellido = apellido
        
self.email
 = email
        
self.tel
 = tel

class ValidadorCliente:
    @staticmethod
    def validar_email(mail):
        return ('@' in mail)

    @staticmethod
    def validar_telefono(telefono):
        return len(telefono) == 10

primer_cliente = Cliente('Gustavo', 'Moya', 'gustavo.moya@bue.edu.ar', '1122334455')

if (ValidadorCliente.validar_telefono(primer_cliente.tel)) :
    print('telefono inválido.')
    tel = input('Vuelva a ingresar el teléfono: ') 