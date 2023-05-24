# Llenar un arreglo de largo n, una vez lleno, pedir un número y buscar si ese número
# se encuentra dentro del arreglo, si se encuentra indicar la posición en donde esta.

import os

array = []
founded = False
while True:
    try:
        cantidad = int(input("Ingrese el largo de la lista: "))
        if cantidad <= 0:
            print("Ingrese una cantidad mayor a 0")
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")


for number in range(cantidad):
    while True:
        try:
            numero = int(input("Ingrese numero: "))
            array.append(numero)
            os.system("cls")
            break
        except ValueError:
            print("Error, caracter no valido")

while True:
    try:
        numeroBuscar = int(input("Ingrese el numero que quiere busar: "))
        os.system("cls")
        break
    except ValueError:
        print("Error, caracter no valido")

for index in range(cantidad):
    if numeroBuscar == array[index]:
        founded = True
        pos = index

if founded == False:
    print("Numero no encontrado")
else: 
    print(f"El {numeroBuscar} se encuentra en la posición {pos} del array")
