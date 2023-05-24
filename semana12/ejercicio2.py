# Crea un arreglo de largo n, pedir además un número entero positivo
# y llenar el arreglo con los múltiplos de ese número. Por ejemplo, si el n es 5 y
# el otro número ingresado es 3 el arreglo deberá tener 3, 6, 9, 12, 15.
# Muestra el arreglo en otro ciclo.

import os

array = []

while True:
    try:
        cantidadNumeros = int(input("Ingrese el largo del arreglo: "))
        numeroArray = int(input("Ingrese el numero con el que desea rellenar: "))
        if cantidadNumeros < 0 or numeroArray < 0:
            print("Ingrese una cantidad positiva")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")


for index in range(cantidadNumeros+1):
    if index != 0:
        array.append(numeroArray * index)

for number in array:
    print(number)


