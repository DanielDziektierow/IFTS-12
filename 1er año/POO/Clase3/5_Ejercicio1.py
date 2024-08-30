#1. Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado.

def SumaPositivos(num):
    if num < 0:     #Si es negativo la funcion no debe servir
        return 0
    else:
        num= num + SumaPositivos(num - 1)   #Si es positivo sumamos el numero de entrada con el retorno de la funcion
        return num
    
# <-- Test -->
n= SumaPositivos(4)
print(n)