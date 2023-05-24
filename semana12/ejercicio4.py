# Llenar dos arreglos de largo n con números enteros.
# Guardar en un tercer arreglo la suma de los elementos del primero y el segundo en la misma posición.
# Ej En el arreglo3, posición 0, quedará, elemento en la posición 0 del arreglo1 + elemento en la posición 0
# del arreglo2).
# Una vez llenos, mostrar el contenido de los 3 arreglos de esta forma.
# valor pos 0 arreglo 1 + valor pos 0 arreglo 2 = valor pos 0 arreglo 3…

import os

array1 = []
array2 = []
array3 = []

while True: 
    try:
        cantidad = int(input("Ingre el largo que desea para la lista 1 y 2: "))
        if cantidad <= 0:
           print("Ingrese una cantidad mayor a 0 ") 
        else:
            os.system("cls")
            break
    except ValueError:
        print("Error, caracter no valido")

for number in range(cantidad):
    while True:
        try:
            numero = int(input("Ingrese numero para lista 1: "))
            array1.append(numero)
            os.system("cls")
            break
        except ValueError:
            print("Error, caracter no valido")

for number in range(cantidad):
    while True:
        try:
            numero = int(input("Ingrese numero para lista 2: "))
            array2.append(numero)
            os.system("cls")
            break
        except ValueError:
            print("Error, caracter no valido")

for index in range(len(array1)):
    array3.append(array1[index] + array2[index])
    
for index in range(len(array3)):
    print(f"La suma de {array1[index]} + {array2[index]} = {array3[index]} ")
