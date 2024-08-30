#2. Escribir una función recursiva que permita mostrar los valores de un vector de atrás hacia adelante.

def VoltearVector(vector):
    i=len(vector)   #Tomamos la cantidad maxima de elementos del vector
    while i > 0:    #Recorremos el vector hasta el primero
        print(vector[i-1])  #i-1 porque las posiciones del vector comienzan por 0
        i= i - 1

# <-- Test -->
v1=["H","O","L","A"]
VoltearVector(v1)