"""3. Composición: Modela un Ordenador que tiene un Procesador, RAM, y Disco Duro.
Implementa las clases correspondientes y muestra cómo un Ordenador puede estar compuesto por estos elementos.
"""
class Procesador:
    def __init__(self, pnombre):
        self.pnombre= pnombre
        
    def mostrar_procesador(self):
        print(self.pnombre)

class Ram:
    def __init__(self, rnombre):
        self.rnombre= rnombre

    def mostrar_ram(self):
        print(self.rnombre)

class DiscoDuro:
    def __init__(self, ddnombre):
        self.ddnombre= ddnombre
    
    def mostrar_discoduro(self):
        print(self.ddnombre)

class Ordenador:
    def __init__(self, marca):
        self.marca= marca
        self.procesador= []
        self.ram= []
        self.discoduro= []
    
    def agregar_procesador(self, pnombre):
        procesador=Procesador(pnombre)
        self.procesador.append(procesador)

    def agregar_ram(self, rnombre):
        ram=Ram(rnombre)
        self.ram.append(ram)

    def agregar_discoduro(self, ddnombre):
        disco=DiscoDuro(ddnombre)
        self.discoduro.append(disco)
    
    def mostrar_todo(self):
        for i in self.procesador:
            i.mostrar_procesador()
        for i in self.discoduro:
            i.mostrar_discoduro()
        for i in self.ram:
            i.mostrar_ram()
        

o1=Ordenador('HP')
o1.agregar_procesador("Intel")
o1.agregar_discoduro("SSD")
o1.agregar_ram("8Gb")
o1.mostrar_todo()