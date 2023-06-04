# Llenar una matriz de n*n con datos, una vez llena, mostrar los elementos de la matriz, por columnas, no por filas.

import random, os

while True:
    try:
        largoMatriz = int(input("Ingrese el tamanno de la matriz: "))
        if largoMatriz <= 0:
            print("Ingrese un valor mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")

matriz = []
for columna in range(largoMatriz):
    fila = []
    for number in range(largoMatriz):
        numero = round(random.random()) * 10
        fila.append(numero)
    matriz.append(fila)

print(matriz)
#Elementos por columna

# 00 01 02
# 10 11 12
# 20 21 22

for i in range(largoMatriz):
    for j in range(largoMatriz):
        print(matriz[j][i])

