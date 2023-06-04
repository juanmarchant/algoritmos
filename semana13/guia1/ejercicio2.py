# 2. Llenar una matriz de largo n*n con nombres, una vez llena la matriz,
# pedir el ingreso de un nombre y buscar cuantas veces se repite ese nombre en la matriz. Mostrar el resultado.

import os

while True: 
    try:
        largoMatriz = int(input("Ingrese el largo de la matriz: n*n -> ")) 
        if largoMatriz <=0:
            print("Ingrese un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")


matriz = []

for largo in range(largoMatriz):
    fila = []
    for nombre in range(largoMatriz):
        nombreColumna  = input("Ingrese nombre: ")
        fila.append(nombreColumna)
    matriz.append(fila)

os.system('cls')

for nombre in matriz:
    print(nombre)

nombreBuscar = input("Ingrese el nombre que le gustaria buscar: ")
contador = 0

for largo in range(largoMatriz):
    for nombre in range(largoMatriz):
        if nombreBuscar == matriz[largo][nombre]:
            contador +=1

if contador != 0:
    print(f"El nombre {nombreBuscar} esta {contador} veces en la matriz")
else:
    print("No se encuentra el nombre")
