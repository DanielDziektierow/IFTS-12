"""5. Escriba una función recursiva para contar en cuantos intentos se puede adivinar el número de un dado. 
Pasos a seguir:
a. Genere un número random
b. Solicite al usuario que ingrese un nro
c. Verifique si es correcto informe que acertó en X intento
d. Si no acertó, cuente el intento y vuelva a solicitar el nro
# Puede utilizar esta librería
para generar los nros random
from random import *
# ...
# ...
n = randint(1,6)"""

from random import *

def AdivinarnDado(nrand, intentos):
    nuser = int(input("Adivine el numero del dado: "))
    if nuser <=0 or nuser >= 7:
        print("Ingresar un numero del 1 al 6.\n")
        AdivinarnDado(nrand, intentos)
    elif nuser == nrand:
        print("Correcto.")
    else:
        intentos=intentos+1
        print(f"Intento: {intentos}")
        AdivinarnDado(nrand,intentos)
    
x = randint(1,6)
AdivinarnDado(x, 0)