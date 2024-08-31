"""
4. Diseña una clase Libro con atributos titulo y autor. 
Incluye un método leer (debe imprimir que el libro está siendo leído). 
Crea una subclase Ebook que herede de Libro y añada un atributo formato 
y un método descargar (debe imprimir que el ebook está siendo descargado). Implementa un método adicional cambiar_formato que permita
cambiar el formato del ebook, verificando que el nuevo formato sea válido (por ejemplo, "PDF", "EPUB", "MOBI").
"""

class Libro:
    def __init__(self,titulo,autor):
        self.titulo= titulo
        self.autor= autor
    
    def Leer(self):
        print(self.titulo+" esta siendo leido...")
    
class Ebook(Libro):
    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato= formato

    def Descargar(self):
        print("El libro "+ self.titulo + " esta siendo descargado...")

    def cambiar_formato(self):
        nuevo_formato= input("Elija el formato de descarga (PDF, EPUB, MOBI)\n")
        if nuevo_formato.find("PDF") >= 0  or nuevo_formato.find("EPUB") >= 0 or nuevo_formato.find("MOBI") >= 0:
            self.formato= nuevo_formato
            print("Eligio el formato "+ self.formato)
        else:
            print("El formato que eligio no es el que tenemos para ofrecer.")
    

eb= Ebook("Sirenita", "Ernesto", "PDF")
eb.cambiar_formato()