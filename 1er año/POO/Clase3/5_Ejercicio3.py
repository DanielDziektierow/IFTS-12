#3. Implementar una función recursiva que permita recorrer una matriz y mostrar sus valores.

def PrintMatriz(matriz):
    for i in range(len(matriz)):            #Recorremos filas de matriz
        for j in range(len(matriz[i])):     #Recorremos columnas de matriz
            print(matriz[i][j])
        print("\n")

# <-- Test -->
mtz=[[1,2,3],[4,5,6],[7,8,9]]
PrintMatriz(mtz)