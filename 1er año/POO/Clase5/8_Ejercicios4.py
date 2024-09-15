"""4. Excepciones personalizadas: Escribe una clase Producto que verifique que el precio ingresado no sea negativo. Si
lo es, lanza una excepción personalizada.
"""

class Producto:
        def __init__(self, precio):     
                try:
                    if precio >= 0:
                            self.precio= precio
                    else:
                          raise ValueError      #Usamos Raise para indicar que se ha producido un error/ condicion especial.
                except ValueError:
                    print("Perdon el numero es negativo.")
                    self.precio=0

# <-- Test -->
p1=Producto(-45)