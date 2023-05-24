# Crea dos arreglos que tengan el mismo tamaño (n),
# en uno de ellos guardarás nombres de personas, en el otro arreglo deberá ir guardando el largo de los nombres.
# Una vez llenos, mostrar el nombre y el largo que tiene.

import os

arrayNombre = []
arrayNombreLongitud = []

while True:
    try:
        cantidadPersonas = int(input("Ingrese cuantas personas ingresara: "))
        if cantidadPersonas < 0:
            print("Ingrese una cantidad positiva")
        else:
            os.system("cls") 
            break
    except ValueError:
        print("Error, caracter no valido")


for personas in range(cantidadPersonas):
    while True:
        try:
            nombre = input("Ingrese el nombre de la persona: ")
            if len(nombre) < 3:
                print("Ingrese un nombre con al menos 3 caracteres")
            else:

                arrayNombre.append(nombre)
                arrayNombreLongitud.append(len(nombre))

                os.system("cls")
                break
        except ValueError:
            print("Error, caracter no valido")

for index, persona in enumerate(arrayNombre):
    print(persona, arrayNombreLongitud[index])
