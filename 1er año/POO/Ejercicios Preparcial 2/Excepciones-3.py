"""3. Implementa una función obtener_edad que solicite al usuario su edad y maneje los errores de ingreso incorrecto. 
Si el usuario ingresa algo que no sea un número, lanza una excepción con un mensaje adecuado.
"""
def obtener_edad():
    try:
        edad= int(input("Ingrese su edad."))
        return edad
    
    except ValueError:
        raise ValueError("Debe ingresar un valor numerico positivo.")

# Ejemplo de uso
try:
    edad = obtener_edad()
    print(f"Edad ingresada: {edad}")
except ValueError as e:
    print(e)