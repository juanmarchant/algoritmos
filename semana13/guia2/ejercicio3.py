# Llenar una matriz no cuadrada, de N*M con números enteros y mostrar la suma de los elementos de la matriz mayores a 20


import os
import random

while True:
    try:
        largoMatriz = int(input("Ingresa el largo de la matriz: "))
        if largoMatriz <=0:
            print("Ingresa un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")

matriz = []
for i in range(largoMatriz+1):
    fila = []
    for j in range(largoMatriz):
        numero =  random.randint(1, 30)
        fila.append(numero)
    matriz.append(fila)

for fila in matriz:
    print(fila)

sumatoria = 0 
for i in range(len(matriz)):
    for j in range(len(matriz)-1):
        if matriz[i][j] > 20:
            sumatoria += matriz[i][j]

print(f"La sumatoria de los numero mayores a 20 en la matriz N*M es: {sumatoria}")
