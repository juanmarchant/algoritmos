# Llenar una matriz cuadrada con números y mostrar todos loselementos que se encuentran en la diagonal secundaria

import random

largoMatriz = random.randint(1,4)
matriz = []
for i in range(largoMatriz):
    fila = []
    for j in range(largoMatriz):
        numero = random.randint(1,10)
        fila.append(numero)
    matriz.append(fila)

for fila in matriz:
    print(fila)

for i in range(largoMatriz):
    for j in range(largoMatriz):
        if i+j == largoMatriz-1:
            print(matriz[i][j])
        

'''
Ejemplo diagional principal
[ ]  [ ] [x]
[ ]  [x] [ ]
[x]  [ ] [ ]
'''
