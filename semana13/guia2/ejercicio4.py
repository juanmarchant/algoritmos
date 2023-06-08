# Llenar una matriz cuadrada con números y mostrar todos los elementos que se encuentran en la diagonal principal



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
        if i== j:
            print(matriz[i][j])

'''
Ejemplo diagional principal
[x]  [ ] [ ]
[ ]  [x] [ ]
[ ]  [ ] [x]
'''

