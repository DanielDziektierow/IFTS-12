"""1. Manejo excepciones: Escribe un programa en Python que solicite al usuario dos números, los sume y maneje la
excepción si se ingresa algo que no es un número.
"""
try:
    n1=int(input("Ingrese el primer numero:\n"))
    n2=int(input("Ingrese el segundo numero:\n"))
    res= n1+n2

except ValueError:
    print("Error: Debes ingresar un número válido.")
else:
    print(f"Resultado: {res}")
finally:
    print("Fin del programa.")