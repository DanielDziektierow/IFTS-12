#4. Dado un nro iniciar una cuenta regresiva por medio de una función recursiva, imprimir la
#cuenta y al llegar a cero imprimir por pantalla "¡Booom!".

def PrintRegresion(num):
    if num < 0:     #Si es negativo la funcion no debe servir
        return 0
    elif num > 0:
        print(num)
        PrintRegresion(num - 1)   #Si es positivo sumamos el numero de entrada con el retorno de la funcion
        return num
    else:
        print("¡Booom!")
        

# <-- Test -->
PrintRegresion(3)