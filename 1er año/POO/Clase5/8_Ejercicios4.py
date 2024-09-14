"""4. Excepciones personalizadas: Escribe una clase Producto que verifique que el precio ingresado no sea negativo. Si
lo es, lanza una excepción personalizada.
"""

class Producto:
        def __init__(self, precio):
                try:
                    if precio >= 0:
                            self.precio= precio
                    else:
                          raise ValueError
                except ValueError:
                    print("Perdon el numero es negativo.")
                    self.precio=0

p1=Producto(45)