# 1. Ingresar n números, donde n es la cantidad ingresada por el usuario.
# • Validar que cada número ingresado sea positivo (mayor a cero).
# • Determine y muestre cual es el número más alto que se haya ingresado.
import os

while True:
    try:
        cantidadNumeros = int(input("Cuantos numeros quiere ingresar? : "))
        if cantidadNumeros < 0: 
            print("Ingrese un cantidad postiva... ex: cantidad > 0 ")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, valor no valido")


contador = 0
numeroMayor = 0

while contador < cantidadNumeros:

    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            if numero < 0: 
                print("Ingrese un numero postivo... ex: numero > 0 ")
            else:
                os.system("cls")
                break
        except ValueError:
            print("Error, valor no valido")

    if contador == 0:
        numeroMayor = numero

    if numero > numeroMayor:
        numeroMayor = numero

    contador =  contador + 1

print(f"El numero mayor es: {numeroMayor}")


