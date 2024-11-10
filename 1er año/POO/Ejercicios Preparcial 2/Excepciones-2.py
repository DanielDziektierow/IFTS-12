"""2. Crea una función leer_archivo que intente leer un archivo y devolver su contenido. 
Si el archivo no existe, lanza una excepción que indique al usuario que el archivo no fue
encontrado."""
def leer_archivo(path):
    try:
        with open(path, 'r') as archivo:
            contenido = archivo.read().strip # Leer archivo
        return contenido
    except FileNotFoundError:
        return "El archivo no fue encontrado. Verifique la ruta."

# Ejemplo de uso
print(leer_archivo("Cuenta microsoft.txt"))  # Reemplaza "archivo.txt" con la ruta de tu archivo
