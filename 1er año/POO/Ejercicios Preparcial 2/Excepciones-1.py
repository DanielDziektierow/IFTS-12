"""1. Escribe una función dividir que tome dos números y devuelva su cociente. 
Si el divisor es cero, lanza una excepción personalizada DivisionPorCeroError con un mensaje
adecuado"""
# Definimos la excepción personalizada
class DivisionPorCeroError(Exception):
    def __init__(self, mensaje):
        self.mensaje ="El divisor, el 2do numero ingresado, no debe ser 0."
        super().__init__(self.mensaje)

# Definimos la función dividir
def dividir(dividendo, divisor):
    if divisor == 0:
        raise DivisionPorCeroError("Error: El divisor, el 2do numero ingresado, no debe ser 0.")
    return dividendo / divisor

# Ejemplo de uso
try:
    resultado = dividir(10, 2)  # Aquí puedes probar con diferentes valores
    print("El resultado de la división es:", resultado)
except DivisionPorCeroError as e:
    print(e)